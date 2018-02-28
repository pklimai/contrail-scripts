#! /usr/bin/python

# This script acknowledges all existing alarms in Contrail system.
# It does not look at alarm state, so alarms that have already been 
# acknowledged are acknowledged again (it does not hurt in lab env.)

import requests
import json
from pprint import pprint

URL_KEYSTONE = "http://172.25.11.4:5000/v2.0/tokens"
URL_ANALYTICS = "http://172.25.11.4:8081/analytics/alarms"
URL_ACK = "http://172.25.11.4:8081/analytics/alarms/acknowledge"

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

if __name__ == "__main__":

    response_keystone = requests.post(URL_KEYSTONE,
            data = json.dumps(payload_keystone), headers = headers)

    response_keystone_parsed = json.loads(response_keystone.text)
    token = response_keystone_parsed["access"]["token"]["id"]

    headers_x_auth = { 
        "X-Auth-Token": token,
        "Content-Type": "application/json" 
    }

    response = requests.get(URL_ANALYTICS, headers = headers_x_auth)

    parsed_resp = json.loads(response.text)

    table = 'vrouter'
    for vr_resp in parsed_resp[table]:
        name = vr_resp['name']
        for alarm in vr_resp['value']['UVEAlarms']['alarms']:
            token = alarm['token']
            type = alarm['type']
            print("Sending ACK: ", table, name, type, token)
            payload_ack = {"table": table, "name": name, "type": type, "token": token}
            ack_resp = requests.post(URL_ACK, data=json.dumps(payload_ack), headers = headers_x_auth)
