import os
from common.yaml_util import YamlUtil
from core.fosapi import FortiOSAPI
from config.settings import CASE_DIR,APICONFIG


class TestClass:
    yaml = YamlUtil()
    FClient = FortiOSAPI()

    def __init__(self):
        data = self.yaml.read_yaml(APICONFIG)
        if data['method'] == 'tokenlogin':
            self.FClient.tokenlogin(host=data['host'], apitoken=data['tokenlogin']['token'])
        else:
            self.FClient.passwdlogin(host=data['host'], username=data['passwdlogin']['username'],
                                password=data['passwdlogin']['password'])

    #添加地址对象
    def test_add_firewall_address(self):
        print("\n-------------------- test_add_firewall_address BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_firewall_address.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_address(vdom=data['vdom'], name=data['name'], subnet=data['subnet'],
                                           associated_interface=data['associated_interface'],
                                           comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_firewall_address END！--------------------\n")

    #查看地址对象
    def test_get_firewall_address(self):
        print("\n-------------------- test_get_firewall_address BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_firewall_address.yaml"))
        res_lst = []
        i = 1
        for data in all:
            res = self.FClient.get_address(name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ',member['name'])
                    try:
                        print('subnet: ',member['subnet'])
                    except KeyError:
                        print(member['name']," don't have subnet!")
                    print('associated-interface: ',member['associated-interface'])
                    print('comment: ',member['comment'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_address END！--------------------\n")

    #修改地址对象
    def test_set_firewall_address(self):
        print("\n-------------------- test_set_firewall_address BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_firewall_address.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_address(vdom=data['vdom'], name=data['name'], new_name=data['new_name'],
                                           subnet=data['subnet'],associated_interface=data['associated_interface'],
                                           comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_address END！--------------------\n")

    #删除地址对象
    def test_del_firewall_address(self):
        print("\n-------------------- test_del_firewall_address BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_firewall_address.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_address(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_address END！--------------------\n")

    #添加地址对象组
    def test_add_address_group(self):
        print("\n-------------------- test_add_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_address_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_address_group(vdom=data['vdom'], name=data['name'], members=data['member'],
                                           comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_address END！--------------------\n")

    #查看地址对象组
    def test_get_address_group(self):
        print("\n-------------------- test_get_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_address_group.yaml"))
        res_lst = []
        i = 1
        for data in all:
            res = self.FClient.get_address_group(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ', member['name'])
                    print('member: ', end='')
                    for el in member['member'][:-1]:
                        print(el['name'],end=', ')
                    print(member['member'][-1]['name'])
                    print('comment: ', member['comment'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_address END！--------------------\n")

    #在地址对象组中添加一个成员
    def test_append_address_group(self):
        print("\n-------------------- test_append_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_append_address_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.append_address_group(vdom=data['vdom'], name=data['name'], member=data['member'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_append_address_group END！--------------------\n")

    #从地址对象组中移除一个成员
    def test_subtract_address_group(self):
        print("\n-------------------- test_subtract_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_subtract_address_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.subtract_address_group(vdom=data['vdom'], name=data['name'], member=data['member'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_subtract_address_group END！--------------------\n")

    #修改地址对象组
    def test_set_address_group(self):
        print("\n-------------------- test_set_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_address_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_address_group(vdom=data['vdom'], name=data['name'], new_name=data['new_name'],
                                                 members=data['member'],comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_address END！--------------------\n")

    #删除地址对象组
    def test_del_address_group(self):
        print("\n-------------------- test_del_address_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_address_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_address_group(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_address END！--------------------\n")

    #添加服务对象
    def test_add_firewall_service(self):
        print("\n-------------------- test_add_firewall_service BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_firewall_service.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_service(vdom=data['vdom'], name=data['name'],protocol=data['protocol'],
                                                 tcp_portrange=data['tcp_portrange'],udp_portrange=data['udp_portrange'],
                                                 sctp_portrange=data['sctp_portrange'],protocol_number=data['protocol_number'],
                                                                                                       comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_firewall_service END！--------------------\n")

    #查看服务对象
    def test_get_firewall_service(self):
        print("\n-------------------- test_get_firewall_service BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_firewall_service.yaml"))
        res_lst = []
        i = 1
        for data in all:
            res = self.FClient.get_service(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ', member['name'])
                    print('protocol: ', member['protocol'])
                    if member['protocol'] == 'TCP/UDP/SCTP':
                        print('tcp-portrange: ',member['tcp-portrange'])
                        print('udp-portrange: ', member['udp-portrange'])
                        print('sctp-portrange: ', member['sctp-portrange'])
                    elif member['protocol'] == 'IP':
                        print('protocol-number: ', member['protocol-number'])
                    print('comment: ', member['comment'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_service END！--------------------\n")

    #修改服务对象
    def test_set_firewall_service(self):
        print("\n-------------------- test_set_firewall_service BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_firewall_service.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_service(vdom=data['vdom'], name=data['name'],new_name=data['new_name'],
                                           protocol=data['protocol'],tcp_portrange=data['tcp_portrange'],
                                           udp_portrange=data['udp_portrange'],sctp_portrange=data['sctp_portrange'],
                                           protocol_number=data['protocol_number'],comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_service END！--------------------\n")

    #删除服务对象
    def test_del_firewall_service(self):
        print("\n-------------------- test_del_firewall_service BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_firewall_service.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_service(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_service END！--------------------\n")

    #添加服务对象组
    def test_add_service_group(self):
        print("\n-------------------- test_add_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_service_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_service_group(vdom=data['vdom'], name=data['name'],
                                                 members=data['member'], comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_service_group END！--------------------\n")

    #查看服务对象组
    def test_get_service_group(self):
        print("\n-------------------- test_get_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_service_group.yaml"))
        res_lst = []
        i = 1
        for data in all:
            res = self.FClient.get_service_group(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ', member['name'])
                    print('member: ', end='')
                    for el in member['member'][:-1]:
                        print(el['name'],end=', ')
                    print(member['member'][-1]['name'])
                    print('comment: ', member['comment'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_service_group END！--------------------\n")

    #修改服务对象组
    def test_set_service_group(self):
        print("\n-------------------- test_set_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_service_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_service_group(vdom=data['vdom'], name=data['name'], new_name=data['new_name'],
                                                 members=data['member'], comment=data['comment'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_service_group END！--------------------\n")

    #在服务对象组中添加一个成员
    def test_append_service_group(self):
        print("\n-------------------- test_append_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_append_service_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.append_service_group(vdom=data['vdom'], name=data['name'], member=data['member'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_append_service_group END！--------------------\n")

    #从服务对象组中移除一个成员
    def test_subtract_service_group(self):
        print("\n-------------------- test_subtract_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_subtract_service_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.subtract_service_group(vdom=data['vdom'], name=data['name'], member=data['member'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_subtract_service_group END！--------------------\n")

    #删除服务对象组
    def test_del_service_group(self):
        print("\n-------------------- test_del_service_group BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_service_group.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_service_group(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_service_group END！--------------------\n")

    #添加NAT地址池
    def test_add_firewall_ippool(self):
        print("\n-------------------- test_add_firewall_ippool BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_firewall_ippool.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_firewall_ippool(vdom=data['vdom'], name=data['name'],
                                                   startip=data['startip'], endip=data['endip'],
                                                   comments=data['comments'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_firewall_ippool END！--------------------\n")

    #查看NAT地址池
    def test_get_firewall_ippool(self):
        print("\n-------------------- test_get_firewall_ippool BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_firewall_ippool.yaml"))
        res_lst = []
        i = 1
        for data in all:
            res = self.FClient.get_firewall_ippool(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ', member['name'])
                    print('startip: ', member['startip'])
                    print('endip: ', member['endip'])
                    print('comments: ', member['comments'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_ippool END！--------------------\n")

    #修改NAT地址池
    def test_set_firewall_ippool(self):
        print("\n-------------------- test_set_firewall_ippool BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_firewall_ippool.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_firewall_ippool(vdom=data['vdom'], name=data['name'], new_name=data['new_name'],
                                                   startip=data['startip'], endip=data['endip'],
                                                   comments=data['comments'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_ippool END！--------------------\n")

    #删除NAT地址池
    def test_del_firewall_ippool(self):
        print("\n-------------------- test_del_firewall_ippool BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_firewall_ippool.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_firewall_ippool(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_ippool END！--------------------\n")

    #添加VIP对象
    def test_add_firewall_vip(self):
        print("\n-------------------- test_add_firewall_vip BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_firewall_vip.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_firewall_vip(vdom=data['vdom'], name=data['name'],
                                                extintf=data['extintf'], extip=data['extip'],
                                                mappedip=data['mappedip'], comment=data['comment'],
                                                portforward=data['portforward'], protocol=data['protocol'],
                                                extport=data['extport'], mappedport=data['mappedport'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_firewall_vip END！--------------------\n")

    #查看VIP对象
    def test_get_firewall_vip(self):
        print("\n-------------------- test_get_firewall_vip BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_firewall_vip.yaml"))
        i = 1
        res_lst = []
        for data in all:
            res = self.FClient.get_firewall_vip(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('name: ', member['name'])
                    print('extintf: ', member['extintf'])
                    print('extip: ', member['extip'])
                    print('mappedip: ', member['mappedip'][0]['range'])
                    print('comment: ', member['comment'])
                    print('portforward: ', member['portforward'])
                    print('protocol: ', member['protocol'])
                    print('extport: ', member['extport'])
                    print('mappedport: ', member['mappedport'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_vip END！--------------------\n")

    #修改VIP对象
    def test_set_firewall_vip(self):
        print("\n-------------------- test_set_firewall_vip BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_firewall_vip.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_firewall_vip(vdom=data['vdom'], name=data['name'], new_name=data['new_name'],
                                                extintf=data['extintf'], extip=data['extip'],
                                                mappedip=data['mappedip'], comment=data['comment'],
                                                portforward=data['portforward'], protocol=data['protocol'],
                                                extport=data['extport'], mappedport=data['mappedport'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_vip END！--------------------\n")

    #删除VIP对象
    def test_del_firewall_vip(self):
        print("\n-------------------- test_del_firewall_vip BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_firewall_vip.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_firewall_vip(vdom=data['vdom'], name=data['name'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_vip END！--------------------\n")

    #添加IPv4策略
    def test_add_firewall_policy(self):
        print("\n-------------------- test_add_firewall_policy BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_add_firewall_policy.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.add_firewall_policy(vdom=data['vdom'], name=data['name'], srcintf=data['srcintf'],
                                                   dstintf=data['dstintf'], srcaddr=data['srcaddr'], dstaddr=data['dstaddr'],
                                                   service=data['service'], action=data['action'], nat=data['nat'],
                                                   poolname=data['poolname'], comments=data['comments'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_add_firewall_policy END！--------------------\n")

    #查看IPv4策略
    def test_get_firewall_policy(self):
        print("\n-------------------- test_get_firewall_policy BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_get_firewall_policy.yaml"))
        i = 1
        res_lst = []
        for data in all:
            res = self.FClient.get_firewall_policy(vdom=data['vdom'], policyid=data['policyid'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('policyid: ', member['policyid'])
                    print('name: ', member['name'])
                    print('srcintf: ', end='')
                    for el in member['srcintf'][:-1]:
                        print(el['name'], end=', ')
                    print(member['srcintf'][-1]['name'])

                    print('dstintf: ', end='')
                    for el in member['dstintf'][:-1]:
                        print(el['name'], end=', ')
                    print(member['dstintf'][-1]['name'])

                    print('srcaddr: ', end='')
                    for el in member['srcaddr'][:-1]:
                        print(el['name'], end=', ')
                    print(member['srcaddr'][-1]['name'])

                    print('dstaddr: ', end='')
                    for el in member['dstaddr'][:-1]:
                        print(el['name'], end=', ')
                    print(member['dstaddr'][-1]['name'])

                    print('service: ', end='')
                    for el in member['service'][:-1]:
                        print(el['name'], end=', ')
                    print(member['service'][-1]['name'])

                    print('action: ', member['action'])
                    print('nat: ', member['nat'])

                    if member['poolname']:
                        print('poolname: ', end='')
                        for el in member['poolname'][:-1]:
                            print(el['name'], end=', ')
                        print(member['poolname'][-1]['name'])
                    print('comments: ', member['comments'])
                    i += 1
        self.check(res_lst)
        print("-------------------- test_get_firewall_policy END！--------------------\n")

    #修改IPv4策略
    def test_set_firewall_policy(self):
        print("\n-------------------- test_set_firewall_policy BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_set_firewall_policy.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.set_firewall_policy(vdom=data['vdom'], policyid=data['policyid'], name=data['name'],
                                                   srcintf=data['srcintf'],dstintf=data['dstintf'], srcaddr=data['srcaddr'],
                                                   dstaddr=data['dstaddr'],service=data['service'], action=data['action'],
                                                   nat=data['nat'], poolname=data['poolname'], comments=data['comments'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_set_firewall_policy END！--------------------\n")

    #删除IPv4策略
    def test_del_firewall_policy(self):
        print("\n-------------------- test_del_firewall_policy BEGIN！--------------------")
        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_del_firewall_policy.yaml"))
        res_lst = []
        for data in all:
            res = self.FClient.del_firewall_policy(vdom=data['vdom'], policyid=data['policyid'])
            res_lst.append(res.status_code)
        self.check(res_lst)
        print("-------------------- test_del_firewall_policy END！--------------------\n")

    def test_monitor_firewall_policy(self):
        print("\n-------------------- test_monitor_firewall_policy BEGIN！--------------------")

        all = self.yaml.read_yaml(os.path.join(CASE_DIR, "test_monitor_firewall_policy.yaml"))
        i = 1
        res_lst = []
        for data in all:
            res = self.FClient.monitor_firewall_policy(vdom=data['vdom'], policyid=data['policyid'])
            res_lst.append(res.status_code)
            if res.status_code == 200:
                result = res.json()['results']
                for member in result:
                    print("\n-----obj" + str(i) + "-----\n")
                    print('policyid: ', member['policyid'])
                    print('bytes: ', member['bytes'])
                    print('packets: ', member['packets'])
                    print('packets: ', member['packets'])
                    print('hit_count: ', member['hit_count'])
                    i += 1
        self.check(res_lst)

        print("-------------------- test_monitor_firewall_policy END！--------------------\n")


    def check(self, res_lst):
        for code in res_lst:
            if code != 200:
                print("\nfailed!\n")
                break
        else:
            print("\nsuccess!\n")

    def __del__(self):
        data = self.yaml.read_yaml(APICONFIG)
        if data['method'] != 'tokenlogin':
            self.FClient.logout()

