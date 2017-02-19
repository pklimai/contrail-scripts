
### Create gateway example

sudo python /opt/contrail/utils/provision_vgw_interface.py --oper create --interface vgw1 --subnets 10.1.0.0/24 --routes 10.10.10.0/24 --vrf default-domain:demo:VN-A:VN-A

### Remove gateway example

sudo python /opt/contrail/utils/provision_vgw_interface.py --oper delete --interface vgw1 --subnets 10.1.0.0/24 --routes 10.10.10.0/24
