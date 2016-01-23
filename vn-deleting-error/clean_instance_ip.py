#! /usr/bin/python

from vnc_api import vnc_api
from pprint import pprint

vnc_lib = vnc_api.VncApi(api_server_host = "10.10.10.230", 
        username = "admin", password = "contrail", tenant_name = "demo",
        auth_host = "10.10.10.230")

#net_list = vnc_lib.virtual_networks_list()
#pprint(net_list)

vn_l = vnc_lib.virtual_network_read(fq_name=['default-domain', 'demo', 'cust-left-vn'])
vn_r = vnc_lib.virtual_network_read(fq_name=['default-domain', 'demo', 'cust-right-vn'])

vn_l_ip_back_refs = vn_l.get_instance_ip_back_refs()
vn_r_ip_back_refs = vn_r.get_instance_ip_back_refs()

print vn_l_ip_back_refs[0]['uuid']
print vn_r_ip_back_refs[0]['uuid']

vnc_lib.instance_ip_delete( id = vn_l_ip_back_refs[0]['uuid'])
vnc_lib.instance_ip_delete( id = vn_r_ip_back_refs[0]['uuid'])
