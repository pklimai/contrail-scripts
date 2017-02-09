curl -s -X POST http://10.10.10.230:5000/v2.0/tokens \
  -H "Content-Type: application/json" \
  -d '{ "auth": { 
     "tenantName": "demo", 
     "passwordCredentials": {
       "username": "admin", 
       "password": "contrail" }}}'      | python -m json.tool
