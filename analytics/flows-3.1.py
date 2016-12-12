#! /usr/bin/python

import requests
import json
from pprint import pprint

headers = { "Content-Type": "application/json" }

payload_keystone = { 
    "auth": { 
        "tenantName": "demo", 
        "passwordCredentials": {
            "username": "admin", 
            "password": "contrail" 
        }
    }
}

response_keystone = requests.post("http://10.10.10.230:5000/v2.0/tokens",
        data = json.dumps(payload_keystone), headers = headers)

token = json.loads(response_keystone.text)

headers_x_auth = { 
    "X-Auth-Token": token["access"]["token"]["id"],
    "Content-Type": "application/json" 
}


payload = { 
    "table": "FlowRecordTable",
    "start_time": "now-1800s",
    "end_time": "now",
    "select_fields": [ "sourceip", "destip" ] 
}

response = requests.post("http://10.10.10.230:8081/analytics/query", 
        data = json.dumps(payload), headers = headers_x_auth)

# print response.text

flows = json.loads(response.text)
# pprint(flows)

talkers = {}

for flow in flows["value"]:
    sip = flow["sourceip"]
    dip = flow["destip"]
    if (sip, dip) not in talkers and (dip, sip) not in talkers:
        talkers[(sip, dip)] = 1
        print "%s <--> %s" % (sip, dip)
        
