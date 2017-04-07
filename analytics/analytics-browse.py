#! /usr/bin/python

import requests
import json
from sys import argv
from pprint import pprint

url_keystone = "http://172.25.11.2:5000/v2.0/tokens"

url_analytics = "http://172.25.11.2:8081"

if len(argv) == 2:
    url_analytics += argv[1]

print("Browsing %s" % url_analytics)

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

response_keystone = requests.post(url_keystone,
        data = json.dumps(payload_keystone), headers = headers)

response_keystone_parsed = json.loads(response_keystone.text)
token = response_keystone_parsed["access"]["token"]["id"]

headers_x_auth = { 
    "X-Auth-Token": token,
    "Content-Type": "application/json" 
}

response = requests.get(url_analytics, headers = headers_x_auth)

pprint(json.loads(response.text))
