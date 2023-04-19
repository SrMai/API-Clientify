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
Buscar.
    Este modulo sirve para buscar cosas relacionadas al CRM.
    De momento solo funciona para filtrar contactos.
"""
#Librerias necesarias para el código
import subprocess as sub
import http.client
import json
import sys
#Importa funciones principales

class Buscar():
    """
        Buscar:
        Este modulo sirve para buscar cosas relacionadas al CRM.
        De momento solo funciona para filtrar contactos.
    """
    def __init__(self):
        super(Buscar, self).__init__()

    def Contacto(token, email, telefono, otros):
        print("Buscando...")
        """
            Buscar contactos:
            Esto funciona ingresado cualquiera de los siguientes datos:
            ♦ Nombre
            ♦ Apellido
            ♦ Email
            ♦ Telefono
        """
        #Verifica si la variable email tiene algun valor
        if email == "N/A":
            #verifica si la variable telefono tiene algun valor
            if telefono == "N/A":
                if otros == "N/A":
                    print("No se puede realizar la busqueda, no hay ningun valor en telefono, ni en email.")
                    sys.exit()
                else:
                    peticion = "?{}".format(otros)
                    mensaje = "Buscando por otros... Peticion: " + peticion
            else:
                #Si hay un valor en telefono, se busca por telefono
                peticion = "?query={}".format(telefono)
                mensaje = "Buscando por telefono... Peticion: " + peticion
                #Comprobar si "otros" tiene de valor "N/A"
                if otros != "N/A":
                    #Si no es "N/A", se busca por "otros"
                    peticion = "?query={}&{}".format(telefono, otros)
                    mensaje = "Buscando por telefono y otros... Peticion: " + peticion
        else:
            #Si hay un valor en email, se busca por email
            peticion = "?query={}".format(email)
            mensaje = "Buscando por email... Peticion: " + peticion
            if telefono != "N/A":
                #Si hay un valor en telefono, se busca por telefono
                peticion = "?query={}&phone={}".format(email, telefono)
                mensaje = "Buscando por email y telefono... Peticion: " + peticion
                if otros != "N/A":
                    #Si no es "N/A", se busca por "otros"
                    peticion = "?query={}&phone={}&{}".format(email, telefono, otros)
                    mensaje = "Buscando por email, telefono y otros... Peticion: " + peticion
            elif otros != "N/A":
                #Si no es "N/A", se busca por "otros"
                peticion = "?query={}&{}".format(email, otros)
                mensaje = "Buscando por Email y otros... Peticion: " + peticion

        #peticion = "?query={}{}{}{}".format(nombre, apellido, email, telefono)
        conn = http.client.HTTPSConnection("api.clientify.net")
        payload = ''
        headers = {
          'Authorization': "Token {}".format(token),
          'Content-Type': 'application/json'      
        }
        conn.request("GET", "/v1/contacts/{}".format(peticion), payload, headers)
        res = conn.getresponse()
        data = res.read()       
        print(mensaje)
        print(data.decode("utf-8"))       
        sys.exit()
    
    def ContactoID(token, ID):
        """
            Buscar contacto por ID:
            Funcion para buscar un contacto con una ID especifica:
            ♦ ID
        """
        conn = http.client.HTTPSConnection("api.clientify.net")
        payload = ''
        headers = {
          'Authorization': "Token {}".format(token)
        }
        conn.request("GET", "/v1/contacts/{}/".format(ID), payload, headers)
        res = conn.getresponse()
        data = res.read()       
        print(data.decode("utf-8"))       
        sys.exit()