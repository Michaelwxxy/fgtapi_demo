import json
import logging
import urllib.request

import requests
import jinja2
from .templates import *
from error_code.http_error_codes import *
from error_code.fos_error_code import error_code
from common.log import Log


# Disable warnings about certificates.
requests.packages.urllib3.disable_warnings()

LOG = Log.create_logger()

class FortiOSAPI:

    def __init__(self):
        self.host = None
        self._session = requests.session()  # use single session
        self._session.verify = False
        self.timeout = 120
        self.cert = None
        self.url_prefix = None
        self._debug = False

    def update_cookie(self):
        # Retrieve server csrf and update session's headers
        LOG.debug("cookies are  : %s ", self._session.cookies)
        for cookie in self._session.cookies:

            if cookie.name == 'ccsrftoken':
                csrftoken = cookie.value[1:-1]  # token stored as a list
                LOG.debug("csrftoken before update  : %s ", csrftoken)
                self._session.headers.update({'X-CSRFTOKEN': csrftoken})
                LOG.debug("csrftoken after update  : %s ", csrftoken)
        LOG.debug("New session header is: %s", self._session.headers)

    #常规账号密码方式
    def passwdlogin(self, host, username, password, https=True, verify=False, timeout=12):
        self.host = host
        if not https:
            self.url_prefix = 'http://' + self.host
        else:
            self.url_prefix = 'https://' + self.host

        url = self.url_prefix + '/logincheck'
        if not self._session:
            self._session = requests.session()
            # may happen if logout is called
        if verify is not False:
            self._session.verify = verify

        self.timeout = timeout

        res = self._session.post(
            url,
            data='username=' + urllib.request.pathname2url(username) + '&secretkey=' + urllib.request.pathname2url(
                password) + "&ajax=1", timeout=self.timeout)

        if res.content.decode('ascii')[0] == '1':
            # Update session's csrftoken
            self.update_cookie()
            return True
        else:
            LOG.error("raw response:  %s ", res.content)
            raise Exception('login failed')

    #apitoken方式
    def tokenlogin(self, host, apitoken, verify=False, https=True, timeout=12):
        self.host = host
        if not self._session:
            self._session = requests.session()
            # may happen at start or if logout is called
        self._session.headers.update({'Authorization': 'Bearer ' + apitoken})
        if not https:
            self.url_prefix = 'http://' + self.host
        else:
            self.url_prefix = 'https://' + self.host

        self._session.verify = verify
        self.timeout = timeout

        return True

    def logout(self):
        try:
            url = self.url_prefix + '/logout'
            self._session.post(url, timeout=self.timeout)
            self._session.close()
            self._session.cookies.clear()
            return True
        except Exception as e:
            LOG.error(e)
            return False

    def format_url(self, path):
        return self.url_prefix + path

    def get(self, path, data):
        url = self.format_url(path)
        return self._session.get(url, params=data)

    def post(self, path, data):
        url = self.format_url(path)
        return self._session.post(url, data=json.dumps(data))

    def put(self, path, data):
        url = self.format_url(path)
        return self._session.put(url, data=json.dumps(data))

    def delete(self, path):
        url = self.format_url(path)
        return self._session.delete(url)

    #模板渲染
    def _render(self, template, **message):
        '''
            :param template: defined API message with essential params.
            :param message: included values of the params for the template
        '''

        if not message:
            message = {}
        msg = jinja2.Template(source=template).render(**message)
        return json.loads(msg)

    #发送请求
    def send_req(self, template, **message):
        template_data = self._render(template, **message)
        path = template_data["path"]
        method = template_data["method"]
        if method == "GET":
            try:
                para = template_data["body"]["json"]
            except KeyError:
                para = {}
            res = self.get(path, para)
            self.checkerror(res)
            return res

        elif method == "POST":
            para = template_data["body"]["json"]
            res = self.post(path, para)
            self.checkerror(res)
            return res

        elif method == "PUT":
            para = template_data["body"]["json"]
            res = self.put(path, para)
            self.checkerror(res)
            return res

        elif method == "DELETE":
            res = self.delete(path)
            self.checkerror(res)
            return res
        else:
            raise Exception("method not support ")

    def checkerror(self,response):
        if response.status_code != SUCCESS_CODE:
            LOG.error("Request : %s on url : %s, body : %s",
                      response.request.method, response.request.url, response.request.body)
            LOG.error("Response : http code %s  reason : %s",
                      response.status_code, http_error_code.get(str(response.status_code)))

            content = json.loads(response.content)
            if content.get('error'):
                code = str(content.get('error'))
                LOG.error("Response : fos code %s reason : %s ", code, error_code.get(code))

            LOG.error("raw response:  %s ", response.content)


#策略相关
    #添加地址对象
    def add_address(self, **message):
        return self.send_req(ADD_FIREWALL_ADDRESS, **message)

    #查看地址对象
    def get_address(self, **message):
        return self.send_req(GET_FIREWALL_ADDRESS, **message)

    #修改地址对象
    def set_address(self, **message):
        return self.send_req(SET_FIREWALL_ADDRESS, **message)

    #删除地址对象
    def del_address(self, **message):
        return self.send_req(DELETE_FIREWALL_ADDRESS, **message)

    #添加地址对象组
    def add_address_group(self, **message):
        return self.send_req(ADD_FIREWALL_ADDRGRP, **message)

    #查看地址对象组
    def get_address_group(self, **message):
        return self.send_req(GET_FIREWALL_ADDRGRP, **message)

    #修改地址对象组
    def set_address_group(self, **message):
        return self.send_req(SET_FIREWALL_ADDRGRP, **message)

    #在地址对象组中添加一个成员
    def append_address_group(self, **message):
        return self.send_req(APPEND_FIREWALL_ADDRESS_TO_ADDRGRP, **message)

    #从地址对象组中移除一个成员
    def subtract_address_group(self, **message):
        return self.send_req(DELETE_FIREWALL_ADDRESS_FROM_ADDRGRP, **message)

    #删除地址对象组
    def del_address_group(self, **message):
        return self.send_req(DELETE_FIREWALL_ADDRGRP, **message)

    #添加服务对象
    def add_service(self, **message):
        return self.send_req(ADD_FIREWALL_SERVICE, **message)

    #查看服务对象
    def get_service(self, **message):
        return self.send_req(GET_FIREWALL_SERVICE, **message)

    #修改服务对象
    def set_service(self, **message):
        return self.send_req(SET_FIREWALL_SERVICE, **message)

    #删除服务对象
    def del_service(self, **message):
        return self.send_req(DELETE_FIREWALL_SERVICE, **message)

    #添加服务对象组
    def add_service_group(self, **message):
        return self.send_req(ADD_FIREWALL_SERVICE_GROUP, **message)

    #查看服务对象组
    def get_service_group(self, **message):
        return self.send_req(GET_FIREWALL_SERVICE_GROUP, **message)

    #修改服务对象组
    def set_service_group(self, **message):
        return self.send_req(SET_FIREWALL_SERVICE_GROUP, **message)

    #在服务对象组中添加一个成员
    def append_service_group(self, **message):
        return self.send_req(APPEND_FIREWALL_SERVICE_TO_SERVGRP, **message)

    #从服务对象组中移除一个成员
    def subtract_service_group(self, **message):
        return self.send_req(DELETE_FIREWALL_SERVICE_FROM_SERVGRP, **message)

    #删除服务对象组
    def del_service_group(self, **message):
        return self.send_req(DELETE_FIREWALL_SERVICE_GROUP, **message)

    #添加NAT地址池
    def add_firewall_ippool(self, **message):
        return self.send_req(ADD_FIREWALL_IPPOOL, **message)

    #查看NAT地址池
    def get_firewall_ippool(self, **message):
        return self.send_req(GET_FIREWALL_IPPOOL, **message)

    #修改NAT地址池
    def set_firewall_ippool(self, **message):
        return self.send_req(SET_FIREWALL_IPPOOL, **message)

    #删除NAT地址池
    def del_firewall_ippool(self, **message):
        return self.send_req(DELETE_FIREWALL_IPPOOL, **message)

    #添加VIP对象
    def add_firewall_vip(self, **message):
        return self.send_req(ADD_FIREWALL_VIP, **message)

    #查看VIP对象
    def get_firewall_vip(self, **message):
        return self.send_req(GET_FIREWALL_VIP, **message)

    #修改VIP对象
    def set_firewall_vip(self, **message):
        return self.send_req(SET_FIREWALL_VIP, **message)

    #删除VIP对象
    def del_firewall_vip(self, **message):
        return self.send_req(DELETE_FIREWALL_VIP, **message)

    #添加IPv4策略
    def add_firewall_policy(self, **message):
        return self.send_req(ADD_FIREWALL_POLICY, **message)

    #查看IPv4策略
    def get_firewall_policy(self, **message):
        return self.send_req(GET_FIREWALL_POLICY, **message)

    #修改IPv4策略
    def set_firewall_policy(self, **message):
        return self.send_req(SET_FIREWALL_POLICY, **message)

    #删除IPv4策略
    def del_firewall_policy(self, **message):
        return self.send_req(DELETE_FIREWALL_POLICY, **message)

    #查看IPv4策略返回的数据
    def monitor_firewall_policy(self, **message):
        return self.send_req(MONITOR_FIREWALL_POLICY, **message)

