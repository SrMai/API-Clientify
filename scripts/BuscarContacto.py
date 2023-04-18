import http.client
import json
import sys

token = sys.argv[1]
nombre = sys.argv[2]
apellido = sys.argv[3]
email = sys.argv[4]
telefono = sys.argv[5]
#Diccionario de telefonos
phones_list = {str(telefono)}



conn = http.client.HTTPSConnection("api.clientify.net")
payload = json.dumps({
  "first_name": "{}".format(nombre),
  "last_name": "{}".format(apellido),
  "email": "{}".format(email),
  "phone": str(telefono),
  "status": "cold-lead",
  "contact_source": "API",
  "last_contact": None
})
headers = {
  'Authorization': "Token {}".format(token),
  'Content-Type': 'application/json'
}
conn.request("GET", "/v1/contacts/?query={}&ID_Facebook=m_LUgK7jBe99VuxHJ8wGtFMo28S3x005tgWo8CKCLy8-Gs5QZItH5BnN7JZNlcWRmnLCJhOzjIzsI-ZjmBfeacoA".format(email), payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))