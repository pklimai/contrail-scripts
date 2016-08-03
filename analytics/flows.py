#! /usr/bin/python

import requests
import json
from pprint import pprint

headers = { "Content-Type": "application/json" }

payload = { 
    "table": "FlowRecordTable",
    "start_time": "now-1800s",
    "end_time": "now",
    "select_fields": [ "sourceip", "destip" ] 
}

response = requests.post("http://10.10.10.230:8081/analytics/query", 
        data = json.dumps(payload), headers = headers )

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
        
