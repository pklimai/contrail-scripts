#! /usr/bin/python

from vnc_api import vnc_api
from pprint import pprint

vnc_lib = vnc_api.VncApi(api_server_host='10.10.10.230',
        auth_host = '10.10.10.230',
        username = "admin",
        password = "contrail",
        tenant_name = "demo")

bgp_routers = vnc_lib.bgp_routers_list()
# pprint(bgp_routers)

for entry in bgp_routers['bgp-routers']: 
    router = vnc_lib.bgp_router_read(entry['fq_name']) 
    pprint(vars(router.bgp_router_parameters))
    
