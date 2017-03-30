
from vnc_api.vnc_api import *

alarm = {
    "alarm_rules": {
        "or_list": [
            {
                "and_list": [
                    {
                        "operand1": "UveVMInterfaceAgent.in_bw_usage",
                        "operation": ">=",
                        "operand2": {
                           "uve_attribute": "1000"
                        }
                    }
                ]
            },
            {
                "and_list": [
                    {
                        "operand1": "UveVMInterfaceAgent.out_bw_usage",
                        "operation": ">=",
                        "operand2": {
                            "uve_attribute": "1000"
                        }
                    }
                ]
            }
        ]
    },
    "alarm_severity": 1,
    "fq_name": [ "default-domain", "demo", "vmi_bw_usage" ],
    "id_perms": {
        "description": "Virtual Machine Interface bw usage greater than 1000"
    },
    "parent_type": "project",
    "uve_keys": {
        "uve_key": [
            "virtual-machine-interface",
        ]
    }
}

vnc_lib = VncApi(api_server_host='10.10.10.230', auth_host = '10.10.10.230', 
        username = "admin", password = "contrail", tenant_name = "demo")

alarm_obj = Alarm(**alarm)
vnc_lib.alarm_create(alarm_obj)
