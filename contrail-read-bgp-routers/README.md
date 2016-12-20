Example output:
---------------
```
root@openstack:~/scripts# python read_bgp_routers.py
{'address': u'10.10.10.231',
 'address_families': family = [u'route-target', u'inet-vpn', u'e-vpn', u'erm-vpn', u'inet6-vpn'],
 'admin_down': False,
 'auth_data': None,
 'autonomous_system': 64512,
 'gateway_address': None,
 'hold_time': 0,
 'identifier': u'10.10.10.231',
 'ipv6_gateway_address': None,
 'local_autonomous_system': None,
 'port': 179,
 'router_type': u'control-node',
 'source_port': None,
 'vendor': u'contrail'}
{'address': u'10.10.10.240',
 'address_families': family = [u'inet-vpn', u'inet6-vpn', u'route-target', u'e-vpn'],
 'admin_down': False,
 'auth_data': None,
 'autonomous_system': 64512,
 'gateway_address': None,
 'hold_time': 90,
 'identifier': u'10.10.10.240',
 'ipv6_gateway_address': None,
 'local_autonomous_system': None,
 'port': 179,
 'router_type': u'router',
 'source_port': None,
 'vendor': u'Juniper'}
 ```
