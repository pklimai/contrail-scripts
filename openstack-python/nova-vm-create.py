#! /usr/bin/python

from novaclient import client

nova = client.Client(version = 2, 
        username = "admin", 
        password = "contrail", 
        project_name = "demo", 
        auth_url = "http://10.10.10.230:5000/v2.0/")

im = nova.images.find(name = "Core-Linux-Image")
fl = nova.flavors.find(name = "Linux-Core")
net_A = nova.networks.find(label = "VN-B")

new_VM = nova.servers.create(name = "VN-B_VM-1", 
        image = im, 
        flavor = fl, 
        nics = [{'net-id': net_A.id}] )

print new_VM

