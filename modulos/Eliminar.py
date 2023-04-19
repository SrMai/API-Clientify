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
Eliminar.
    Este modulo sirve para eliminar cosas relacionadas al CRM.
    De momento solo funciona para eliminar contactos.
"""

#Librerias necesarias para el código
import subprocess as sub
import http.client
import json
import sys
#Importa funciones principales

class Eliminar():
    """
        Eliminar.
            Este modulo sirve para eliminar cosas relacionadas al CRM.
            De momento solo funciona para eliminar contactos.
    """
    def __init__(self):
        super(Eliminar, self).__init__()

    def Contacto(token, id):
        """
            Eliminar contacto:
            Datos necesarios:
            ♦ ID del contacto           
        """
        conn = http.client.HTTPSConnection("api.clientify.net")
        payload = ''
        headers = {
          'Authorization': "Token {}".format(token),
          'Content-Type': 'application/json'
        }
        conn.request("DELETE", "/v1/contacts/{}/".format(id), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print("Accion ejecutada. " + data.decode("utf-8"))
        sys.exit()