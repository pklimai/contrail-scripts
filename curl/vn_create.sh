curl -X POST -H "Content-Type: application/json; charset=UTF-8" -H "X-Auth-Token: 5a56fb6533ef43ec94c03de8bbe22fcf" \
-d '{"virtual-network": {
       "parent_type": "project", 
       "fq_name": ["default-domain", "demo", "VN-A"], 
       "network_ipam_refs": [ {
           "attr": {"ipam_subnets": [{"subnet": {"ip_prefix": "10.1.0.0", "ip_prefix_len": 24}}]}, 
           "to": ["default-domain", "default-project", "default-network-ipam"]
       }]}}' http://10.10.10.230:8082/virtual-networks | python -m json.tool
