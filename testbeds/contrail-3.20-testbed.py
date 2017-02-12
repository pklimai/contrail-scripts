from fabric.api import env

# FOR LAB ONLY, DEFAULT IS 250
minimum_diskGB = 10

# MANAGEMENT USERNAME/IP ADDRESSES
host1 = 'root@172.25.11.2'
host2 = 'root@172.25.11.3'
host3 = 'root@172.25.11.4'
host4 = 'root@172.25.11.5'
host5 = 'root@172.25.11.6'

# EXTERNAL ROUTER DEFINITIONS
ext_routers = []

# AUTONOMOUS SYSTEM NUMBER
router_asn = 64512

# HOST FROM WHICH THE FAB COMMANDS ARE TRIGGERED
# TO INSTALL AND PROVISION
host_build = 'root@172.25.11.2'

# ROLE DEFINITIONS
env.roledefs = {
    'all': [host1, host2, host3, host4, host5],
    'cfgm': [host1],
    'openstack': [host1],
    'control': [host2],
    'compute': [host3, host4, host5],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build]
}

# DOCKER
env.hypervisor = {
    host5 : 'docker',
}

# NODE HOSTNAMES
env.hostnames = {
    'host1': ['openstack'],
    'host2': ['control'],
    'host3': ['compute-1'],
    'host4': ['compute-2'],
    'host5': ['compute-3'],
}

# OPENSTACK ADMIN PASSWORD
env.openstack_admin_password = 'contrail'

# NODE PASSWORDS
env.passwords = {
    host1: 'contrail',
    host2: 'contrail',
    host3: 'contrail',
    host4: 'contrail',
    host5: 'contrail',    
    host_build: 'contrail',
}
