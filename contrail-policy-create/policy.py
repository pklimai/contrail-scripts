#! /usr/bin/python

from vnc_api import vnc_api

vnc_lib = vnc_api.VncApi(api_server_host='10.10.10.230', 
        auth_host = '10.10.10.230', 
        username = "admin", 
        password = "contrail", 
        tenant_name = "demo")

prj = vnc_lib.project_read(fq_name=['default-domain', 'demo'])
vnA = vnc_lib.virtual_network_read(fq_name=['default-domain', 'demo', 'VN-A'])
vnB = vnc_lib.virtual_network_read(fq_name=['default-domain', 'demo', 'VN-B'])

vnA_name = vnA.get_fq_name_str()
vnB_name = vnB.get_fq_name_str()

print "Working with networks %s and %s" % (vnA_name, vnB_name)

policy = vnc_api.NetworkPolicy('VN-A_to_VN-B', parent_obj = prj,
  network_policy_entries = vnc_api.PolicyEntriesType(
    [ 
    vnc_api.PolicyRuleType(
      direction='<>', 
      action_list = vnc_api.ActionListType(simple_action="pass"), 
      protocol = 'any', 
      src_addresses = [vnc_api.AddressType(virtual_network = vnA_name)],
      src_ports = [vnc_api.PortType(-1, -1)],
      dst_addresses = [vnc_api.AddressType(virtual_network = vnB_name)], 
      dst_ports = [vnc_api.PortType(-1, -1)]
      )
    ]
  )
)

vnA.add_network_policy(policy, vnc_api.VirtualNetworkPolicyType(
    sequence = vnc_api.SequenceType(0, 0)))
vnB.add_network_policy(policy, vnc_api.VirtualNetworkPolicyType(
    sequence=vnc_api.SequenceType(0, 0)))

result_policy_create = vnc_lib.network_policy_create(policy)
result_A = vnc_lib.virtual_network_update(vnA)
result_B = vnc_lib.virtual_network_update(vnB)

print "\nPolicy created: %s\n" % result_policy_create
print "Update netwok VN-A result: \n %s \n" % result_A
print "Update netwok VN-B result: \n %s \n" % result_B


