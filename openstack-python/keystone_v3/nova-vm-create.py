#! /usr/bin/python

import os

from keystoneauth1 import identity, session
from novaclient import client

auth = identity.v3.Password(auth_url=os.environ['OS_AUTH_URL'],
       username=os.environ['OS_USERNAME'],
       password=os.environ['OS_PASSWORD'],
       project_name="demo",
       user_domain_id=os.environ['OS_USER_DOMAIN_NAME'],
       project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'])

sess = session.Session(auth=auth, verify=False)

nova = client.Client(version=2, session=sess)

im = nova.images.find(name="cirros-image")
fl = nova.flavors.find(name="cirros-flavor")
net_A = nova.networks.find(label="VN-A")

new_VM = nova.servers.create(name="VM-A1-Python",
        image=im, flavor=fl, nics=[{'net-id': net_A.id}] )

print new_VM
