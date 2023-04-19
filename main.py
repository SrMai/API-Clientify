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
    
    Filtro para conocer la entrada de texto del usuario al escribir en la consola y ejecutar el programa en la funcion correspondiente.

"""
#Librerias necesarias para el código
import sys

#Importa funciones principales
from modulos.Buscar import Buscar as Buscar
from modulos.Crear import Crear as Crear
from modulos.Eliminar import Eliminar as Eliminar

#Filtro
if len(sys.argv) > 1:
    if (sys.argv[1] in ["buscar", "--buscar"]):
        Buscar.Contacto(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif (sys.argv[1] in ["buscar_id", "--buscar_id"]):
        Buscar.ContactoID(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] in ["crear", "--crear"]):
        Crear.Contacto(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif (sys.argv[1] in ["nota", "--nota"]):
        Crear.Nota(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif (sys.argv[1] in ["eliminar", "--eliminar"]):
        Eliminar.Contacto(sys.argv[2], sys.argv[3])
    else:
        print("No se reconoce la petición.")