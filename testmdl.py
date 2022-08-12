import pymailtm
import random
import requests
import json
p = pymailtm.MailTm()
password = p._generate_password(8)
domain = str(random.choice(p._get_domains_list()))
create = p._make_account_request("accounts",p._generate_password(12).lower() + '@' + domain, password)
address = create["address"]
_id = create["id"]
x = pymailtm.Account("62f6284bf2b800e19b01940a", "e6wcaqgsisw4@arxxwalls.com", "V798DFSM")
r = requests.get("{}/messages?page={}".format(p.api_address, "1"),
                         headers=x.auth_headers).text
for message_data in json.loads(r)["hydra:member"]:
    r = requests.get(f"{p.api_address}/messages/{message_data['id']}", headers=x.auth_headers).text
    print(r)