#! /usr/bin/python

from novaclient import client

nova = client.Client(version = 2, 
        username = "admin", 
        api_key = "contrail", 
        project_id = "demo", 
        auth_url = "http://10.10.10.230:5000/v2.0/")

VMs = nova.servers.list()

for VM in VMs: 
    print "Name = %s, Status = %s, Networks = %s" % (
        VM.name, VM.status, VM.networks)
