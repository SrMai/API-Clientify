"""
Copyright (c) 2023 Carlos Adrian Ayala Gonzalez
All rights reserved.

Github: SrMai | carlosayala.cloud | srmai.github.io
Linkedin: linkedin.com/in/carlosayala04/
"""

import sys
import requests

token = sys.argv[1]
contact_id = sys.argv[2]
name = sys.argv[3]
comment = sys.argv[4]

headers = {
    "Authorization": "Token {}".format(token),
    "Content-Type": "application/json"
}

data = {
    "name": name,
    "comment": comment
}

url = "https://api.clientify.net/v1/contacts/{}/note/".format(contact_id)

response = requests.post(url, headers=headers, json=data)

print(response.text)
