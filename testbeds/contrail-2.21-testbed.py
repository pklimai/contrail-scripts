from fabric.api import env

# FOR LAB ONLY, DEFAULT IS 250
minimum_diskGB = 10

# MANAGEMENT USERNAME/IP ADDRESSES
host1 = 'root@10.10.10.230'
host2 = 'root@10.10.10.231'
host3 = 'root@10.10.10.233'
host4 = 'root@10.10.10.234'

# EXTERNAL ROUTER DEFINITIONS
ext_routers = []

# AUTONOMOUS SYSTEM NUMBER
router_asn = 64512

# HOST FROM WHICH THE FAB COMMANDS ARE TRIGGERED
# TO INSTALL AND PROVISION
host_build = 'root@10.10.10.230'

# ROLE DEFINITIONS
env.roledefs = {
    'all': [host1, host2, host3, host4],
    'cfgm': [host1],
    'openstack': [host1],
    'control': [host2],
    'compute': [host3, host4],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build],
    'storage-master': [host1],
    'storage-compute': [host3, host4],
}

# NODE HOSTNAMES
env.hostnames = {
    'host1': ['openstack'],
    'host2': ['control1'],
    'host3': ['compute1'],
    'host4': ['compute2'],
}

# OPENSTACK ADMIN PASSWORD
env.openstack_admin_password = 'contrail'

# NODE PASSWORDS
env.passwords = {
    host1: 'contrail',
    host2: 'contrail',
    host3: 'contrail',
    host4: 'contrail',
    host_build: 'contrail',
}

# FOR REIMAGE PURPOSES
env.ostypes = {
    host1: 'ubuntu',
    host2: 'ubuntu',
    host3: 'ubuntu',
    host4: 'ubuntu',
}
