import http
import json
import requests
nombre = "Carlos"
apellido = "Ayala"
email = "asddasd@gmail.com"
telefono = "123123123"
token = "b02655bd6a3d03900958f1d8b53231098a880a81"
conn = http.client.HTTPSConnection("api.clientify.net")
payload = json.dumps({
  "first_name": "{}".format(nombre),
  "last_name": "{}".format(apellido),
  "email": "{}".format(email),
  "phone": str(telefono),
  "status": "cold-lead",
  "contact_source": "API",
  "last_contact": None,
  "facebook_id": "1234"
})
headers = {
  'Authorization': "Token {}".format(token),
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/contacts/", payload, headers)
res = conn.getresponse()
data = res.read()
if data.decode("utf-8") == " ":
    print("[ERROR] No se pudo crear el contacto. " + data.decode("utf-8"))
else: 
    print("Contacto creado correctamente. " + data.decode("utf-8"))