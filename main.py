import requests
requests.packages.urllib3.disable_warnings()

from testcase.test_fortiosapi import TestClass

test = TestClass()

if __name__ == '__main__':
    # test.test_get_address_group()
    # test.test_add_firewall_address()
    test.test_get_firewall_address()
    # test.test_set_firewall_address()
    # test.test_del_firewall_address()
    #
    # test.test_add_address_group()
    # test.test_get_address_group()
    # test.test_set_address_group()
    # test.test_append_address_group()
    # test.test_subtract_address_group()
    # test.test_del_address_group()
    #
    # test.test_add_firewall_service()
    # test.test_get_firewall_service()
    # test.test_set_firewall_service()
    # test.test_del_firewall_service()
    #
    # test.test_add_service_group()
    # test.test_get_service_group()
    # test.test_set_service_group()
    # test.test_append_service_group()
    # test.test_subtract_service_group()
    # test.test_del_service_group()
    #
    # test.test_add_firewall_ippool()
    # test.test_get_firewall_ippool()
    # test.test_set_firewall_ippool()
    # test.test_del_firewall_ippool()
    #
    # test.test_add_firewall_vip()
    # test.test_get_firewall_vip()
    # test.test_set_firewall_vip()
    # test.test_del_firewall_vip()
    #
    # test.test_add_firewall_policy()
    # test.test_get_firewall_policy()
    # test.test_set_firewall_policy()
    # test.test_del_firewall_policy()
    test.test_monitor_firewall_policy()