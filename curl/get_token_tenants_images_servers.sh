curl -s -X POST http://192.168.24.15:5000/v2.0/tokens \
 -H "Content-Type: application/json" \
 -d '{ "auth": { 
    "tenantName": "demo", 
    "passwordCredentials": {
      "username": "admin", 
      "password": "bjXUPpgUpjxTdeEJnW3AttMYE" }}}' \
| python -m json.tool


curl -s -H "X-Auth-Token: 227cda3bc0da4df49a3eb97083d70ff2" \
   http://192.168.24.15:5000/v2.0/tenants | python -m json.tool

   
curl -s -H "X-Auth-Token: 227cda3bc0da4df49a3eb97083d70ff2" http://192.168.24.19:9292/v2/images | python -m json.tool


curl -s -H "X-Auth-Token: 4cbbab53e94b423da5a373f85de7b9dc" \
  http://192.168.24.19:8774/v2/653a96267be6457bbbdf5edd70848b7f/servers \
| python -m json.tool

