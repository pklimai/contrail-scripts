The script clean_instance_ip.py fixes the following error that sometimes happens when you try to delete a 
virtual network from GUI (probably the problem is related to using Heat templates in an incorrect manner):

Error in deleting networks - cust-left-vn, cust-right-vn

Network: cust-left-vn

Back-References from http://10.10.10.230:9100/instance-ip/452ae295-e988-481c-8263-5fa28a73bb09 still exist

Network: cust-right-vn

Back-References from http://10.10.10.230:9100/instance-ip/b7b414ff-0d7f-49b6-aff5-9bdc002587d0 still exist
