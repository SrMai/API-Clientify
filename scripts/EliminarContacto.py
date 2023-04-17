"""
Copyright (c) 2023 Carlos Adrian Ayala Gonzalez
All rights reserved.

Github: SrMai | carlosayala.cloud | srmai.github.io
Linkedin: linkedin.com/in/carlosayala04/
"""

import http.client
import json
import sys

token = sys.argv[1]
eliminar_contacto_id = sys.argv[2]

conn = http.client.HTTPSConnection("api.clientify.net")
payload = ''
headers = {
  'Authorization': "Token {}".format(token),
  'Content-Type': 'application/json'
}
conn.request("DELETE", "/v1/contacts/{}/".format(eliminar_contacto_id), payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


