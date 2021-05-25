#添加地址对象
ADD_FIREWALL_ADDRESS = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/address?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/address",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            {% if associated_interface %}
                "associated-interface": "{{ associated_interface }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "subnet": "{{ subnet }}",
            "name": "{{ name }}"
        }
    }
}
"""

#查看地址对象
GET_FIREWALL_ADDRESS = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/address/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/address/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/address/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/address/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改地址对象
SET_FIREWALL_ADDRESS = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/address/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/address/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json": {
            {% if associated_interface %}
                "associated-interface": "{{ associated_interface }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            {% if subnet %}
                "subnet": "{{ subnet }}",
            {% endif %}
            {% if new_name %}
                "name": "{{ new_name }}"
            {% else %}
                "name": "{{ name }}"
            {% endif %}
        }
    }
}
"""

#删除地址对象
DELETE_FIREWALL_ADDRESS = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/address/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/address/{{ name }}",
    {% endif %}
    "method": "DELETE"
}
"""

#添加地址对象组
#json数据最后不能有”,“，因此将members[-1]从for循环中拿出来
ADD_FIREWALL_ADDRGRP = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/addrgrp?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/addrgrp/",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            "name": "{{ name }}",
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "member": [
            {% for member in members[:-1] %}
                {
                    "name": "{{ member }}"
                },
            {% endfor %}
                {
                    "name": "{{ members[-1] }}"
                }
            ]
        }
    }
}
"""

#查看地址对象组
GET_FIREWALL_ADDRGRP = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/addrgrp/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/addrgrp/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改地址对象组
SET_FIREWALL_ADDRGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json":{
            {% if new_name %}
                "name": "{{ new_name }}",
            {% else %}
                "name": "{{ name }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "member": [
                {% for member in members[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ members[-1] }}"
                    }
            ]
        } 
    }
}
"""

#给地址对象组添加一个成员
APPEND_FIREWALL_ADDRESS_TO_ADDRGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/member?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/member",
    {% endif %}
    "method": "POST",
    "body": {
        "json":{
            "name": "{{ member }}"
        }
    }
}
"""


#从地址对象组中移除一个成员
DELETE_FIREWALL_ADDRESS_FROM_ADDRGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/member/{{ member }}?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/member/{{ member }}",
    {% endif %}
    "method": "DELETE"
}
"""

#删除地址对象组
DELETE_FIREWALL_ADDRGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/addrgrp/{{ name }}",
    {% endif %}
    "method": "DELETE"
}
"""


#添加服务对象
ADD_FIREWALL_SERVICE = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/custom?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/custom",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            {% if protocol is defined %}
                "protocol": "{{ protocol }}",
            {% else %}
                "protocol": "TCP/UDP/SCTP",
            {% endif %}
            {% if protocol == "TCP/UDP/SCTP" %}
                "tcp-portrange": "{{ tcp_portrange }}",
                "udp-portrange": "{{ udp_portrange }}",
                "sctp-portrange": "{{ sctp_portrange }}",
            {% elif protocol == "IP" %}
                "protocol-number": "{{ protocol_number }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "name": "{{ name }}"
        }
    }
}
"""

#查看服务对象
GET_FIREWALL_SERVICE = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall.service/custom/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall.service/custom/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改服务对象
SET_FIREWALL_SERVICE = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json": {
            {% if protocol is defined %}
                "protocol": "{{ protocol }}",
            {% else %}
                "protocol": "TCP/UDP/SCTP",
            {% endif %}
            {% if protocol == "TCP/UDP/SCTP" %}
                "tcp-portrange": "{{ tcp_portrange }}",
                "udp-portrange": "{{ udp_portrange }}",
                "sctp-portrange": "{{ sctp-portrange }}",
            {% elif protocol == "IP" %}
                "protocol-number": "{{ protocol_number }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            {% if new_name %}
                "name": "{{ new_name }}"
            {% else %}
                "name": "{{ name }}"
            {% endif %}
        }
    }
}
"""

#删除服务对象
DELETE_FIREWALL_SERVICE = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/custom/{{ name }}",
    {% endif %}
    "method": "DELETE"
}
"""


#添加服务对象组
ADD_FIREWALL_SERVICE_GROUP = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall.service/group?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall.service/group",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            "name": "{{ name }}",
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "member": [
            {% for member in members[:-1] %}
                {
                    "name": "{{ member }}"
                },
            {% endfor %}
                {
                    "name": "{{ members[-1] }}"
                }
            ]
        }
    }
}
"""

#查看服务对象组
GET_FIREWALL_SERVICE_GROUP = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall.service/group/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall.service/group/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改服务对象组
SET_FIREWALL_SERVICE_GROUP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json":{
            {% if new_name %}
                "name": "{{ new_name }}",
            {% else %}
                "name": "{{ name }}",
            {% endif %}
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            "member": [
                {% for member in members[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ members[-1] }}"
                    }
            ]
        } 
    }
}
"""


#给服务对象组添加一个成员
APPEND_FIREWALL_SERVICE_TO_SERVGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/member?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/member",
    {% endif %}
    "method": "POST",
    "body": {
        "json":{
            "name": "{{ member }}"
        }
    }
}
"""


#从服务对象组中移除一个成员
DELETE_FIREWALL_SERVICE_FROM_SERVGRP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/member/{{ member }}?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/member/{{ member }}",
    {% endif %}
    "method": "DELETE"
}
"""


#删除服务对象组
DELETE_FIREWALL_SERVICE_GROUP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall.service/group/{{ name }}",
    {% endif %}
    "method": "DELETE"
}
"""

#添加NAT地址池
ADD_FIREWALL_IPPOOL = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/ippool?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/ippool",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            "startip": "{{ startip }}",
            {% if endip %}
                "endip": "{{ endip }}",
            {% else %}
                "endip": "{{ startip }}",
            {% endif %}
            "type": "overload",
            {% if comments %}
                "comments": "{{ comments }}",
            {% endif %}
            {% if name %}
                "name": "{{ name }}"
            {% endif %}
        }
    }
}
"""

#查看NAT地址池
GET_FIREWALL_IPPOOL = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/ippool/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/ippool/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/ippool/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/ippool/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改NAT地址池
SET_FIREWALL_IPPOOL = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/ippool/{{ name }}?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/ippool/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json": {
            "startip": "{{ startip }}",
            {% if endip %}
                "endip": "{{ endip }}",
            {% else %}
                "endip": "{{ startip }}",
            {% endif %}
            "type": "overload",
            {% if new_name %}
                "name": "{{ new_name }}",
            {% else %}
                "name": "{{ name }}",
            {% endif %}
            {% if comments %}
                "comments": "{{ comments }}"
            {% endif %}
        }
    }
}
"""


#删除NAT地址池
DELETE_FIREWALL_IPPOOL = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/ippool/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/ippool/{{ name }}/",
    {% endif %}
    "method": "DELETE"
}
"""

#添加VIP对象
ADD_FIREWALL_VIP = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/vip?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/vip",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            "name": "{{ name }}",
            "extip": "{{ extip }}",
            {% if extintf %}
                "extintf": "{{ extintf }}",
            {% else %}
                "extintf": "any",
            {% endif %}
            "mappedip": [
            {
                    "range": "{{ mappedip }}"
            }
            ],
            "type": "static-nat",
            {% if comment %}
                "comment": "{{ comment }}",
            {% endif %}
            {% if portforward == "enable" %}
                "portforward": "enable",
                "protocol":"{{ protocol }}",
                "extport": "{{ extport }}",
                "mappedport": "{{ mappedport }}"
            {% else %}
                "portforward": "disable"
            {% endif %}
        }
    }
}
"""

#查看VIP对象
GET_FIREWALL_VIP = """
{
    {% if name %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/vip/{{ name }}/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/vip/{{ name }}/",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/vip/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/vip/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""


#修改VIP对象
SET_FIREWALL_VIP = """
{
    {% if vdom %}
        "path":"/api/v2/cmdb/firewall/vip/{{ name }}?vdom={{ vdom }}",
    {% else %}
        "path":"/api/v2/cmdb/firewall/vip/{{ name }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json": {
            "extip": "{{ extip }}",
            {% if extintf %}
                "extintf": "{{ extintf }}",
            {% else %}
                "extintf": "any",
            {% endif %}
            {% if new_name %}
                "name": "{{ new_name }}",
            {% else %}
                "name": "{{ name }}",
            {% endif %}
            "mappedip": [
            {
                    "range": "{{ mappedip }}"
            }
            ],
            "type": "static-nat",
            {% if portforward == "enable" %}
                "portforward": "enable",
                "protocol":"{{ protocol }}",
                "extport": "{{ extport }}",
                "mappedport": "{{ mappedport }}"
            {% else %}
                "portforward": "disable"
            {% endif %}
        }
    }
}
"""

#删除VIP对象
DELETE_FIREWALL_VIP = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/vip/{{ name }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/vip/{{ name }}",
    {% endif %}
    "method": "DELETE"
}
"""

#添加IPv4策略
ADD_FIREWALL_POLICY = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/policy?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/policy",
    {% endif %}
    "method": "POST",
    "body": {
        "json": {
            "name": "{{ name }}",
            "srcintf": [
                {% for member in srcintf[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ srcintf[-1] }}"
                    }
            ],
            "dstintf": [
                {% for member in dstintf[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ dstintf[-1] }}"
                    }
            ],
            "srcaddr":  [
                {% for member in srcaddr[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ srcaddr[-1] }}"
                    }
            ],
            "dstaddr":  [
                {% for member in dstaddr[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ dstaddr[-1] }}"
                    }
            ],
            "service":  [
                {% for member in service[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ service[-1] }}"
                    }
            ],
            "action": "{{ action }}",
            "schedule": "always",
            "nat": "{{ nat }}",
            {% if nat == "enable" %}
                {% if poolname %}             
                    "ippool": "enable",
                    "poolname":[
                        {% for member in poolname[:-1] %}
                            {
                                "name": "{{ poolname }}"
                            },
                        {% endfor %}
                            {
                                "name": "{{ poolname[-1] }}"
                            }
                        ],
                {% endif %}
            {% endif %}
            "status": "enable",
            {% if comments %}
                "comments": "{{ comments }}"
            {% endif %}
        }
    }
}
"""


#查看IPv4策略
GET_FIREWALL_POLICY = """
{
    {% if policyid %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}",
        {% endif %}
    {% else %}
        {% if vdom %}
            "path": "/api/v2/cmdb/firewall/policy/?vdom={{ vdom }}",
        {% else %}
            "path": "/api/v2/cmdb/firewall/policy/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

#修改IPv4策略
SET_FIREWALL_POLICY = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}",
    {% endif %}
    "method": "PUT",
    "body": {
        "json": {
            {% if name %}
                "name": "{{ name }}",
            {% endif %}
            "srcintf": [
                {% for member in srcintf[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ srcintf[-1] }}"
                    }
            ],
            "dstintf": [
                {% for member in dstintf[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ dstintf[-1] }}"
                    }
            ],
            "srcaddr":  [
                {% for member in srcaddr[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ srcaddr[-1] }}"
                    }
            ],
            "dstaddr":  [
                {% for member in dstaddr[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ dstaddr[-1] }}"
                    }
            ],
            "service":  [
                {% for member in service[:-1] %}
                    {
                        "name": "{{ member }}"
                    },
                {% endfor %}
                    {
                        "name": "{{ service[-1] }}"
                    }
            ],
            "action": "{{ action }}",
            "schedule": "always",
            "nat": "{{ nat }}",
            {% if nat == "enable" %}
                {% if poolname %}             
                    "ippool": "enable",
                    "poolname":[
                        {% for member in poolname[:-1] %}
                            {
                                "name": "{{ poolname }}"
                            },
                        {% endfor %}
                            {
                                "name": "{{ poolname[-1] }}"
                            }
                        ],
                {% endif %}
            {% endif %}
            "status": "enable",
            {% if comments %}
                "comments": "{{ comments }}"
            {% endif %}
        }
    }
}
"""

#删除IPv4策略
DELETE_FIREWALL_POLICY = """
{
    {% if vdom %}
        "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/cmdb/firewall/policy/{{ policyid }}",
    {% endif %}
    "method": "DELETE"
}
"""

#查看ipv4策略返回的数据
MONITOR_FIREWALL_POLICY = """
{
    {% if vdom %}
        "path": "/api/v2/monitor/firewall​/policy/?vdom={{ vdom }}",
    {% else %}
        "path": "/api/v2/monitor/firewall/policy/",
    {% endif %}
    "method": "GET",
    "body": {
        "json": {
            "policyid": "{{ policyid }}"
        }
    }
}
"""
