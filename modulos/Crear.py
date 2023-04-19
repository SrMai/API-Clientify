###################################################################################
#             Copyright (c) 2023 Carlos Adrian Ayala Gonzalez
#                         All rights reserved.
#             
#             Github: SrMai | carlosayala.cloud | srmai.github.io
#                 Linkedin: linkedin.com/in/carlosayala04/
###################################################################################

"""
Documentación del API:
    https://github.com/SrMai/API-Clientify
Crear.
    Este modulo sirve para crear cosas relacionadas al CRM.
    De momento solo funciona para crear contactos y notas.
"""

#Librerias necesarias para el código
import subprocess as sub
import http.client
import json
import sys
import requests
#Importa funciones principales

class Crear():
    """
        Crear.
            Este modulo sirve para crear cosas relacionadas al CRM.
        De momento solo funciona para crear contactos y notas.
    """
    def __init__(self):
        super(Crear, self).__init__()

    def Contacto(token, nombre, apellido, email, telefono):
        """
            Crear contacto:
            Esto funciona ingresado los siguientes datos:
            ♦ Nombre
            ♦ Apellido
            ♦ Email
            ♦ Telefono
        """
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
        sys.exit()

    def Nota(token, contact_id, name, comment):
        """
            Crear nota:
            Esto funciona ingresado los siguientes datos:
            ♦ ID del contacto
            ♦ Nombre de la nota
            ♦ Comentario de la nota
        """
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
        if data.decode("utf-8") == " ":
            print("[ERROR] No se pudo crear la nota. " + data.decode("utf-8"))
        else: 
            print("Nota creada correctamente. " + data.decode("utf-8"))
        sys.exit()