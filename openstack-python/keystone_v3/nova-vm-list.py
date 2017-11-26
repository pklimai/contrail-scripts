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

VMs = nova.servers.list()

for VM in VMs:
    print "Name = %s, Status = %s, Networks = %s" % (
            VM.name, VM.status, VM.networks)
            
