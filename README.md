# API-Clientify
 Código para consumir API para clientify con python y/o php

Objetivo:
Crear un codigo que funcione con solo motodos _GET para poder hacer consultas, crear, eliminar y modificar desde una peticion con una URL.

Instalación:
• Clona el repositorio
• Abre el archivo routes.php
• En la variable $token coloca tu clave API
• Ya podras hacer consultas con _GET

Funciones: actuales
♦ Crear
    •Contactos
        URL.php?crear_contacto_nombre=Nombre&crear_contacto_apellido=Apellido&crear_contacto_email=admin@gmail.com&crear_contacto_telefono=1234567890
    •Notas
        URL.php?nota_id=43070872&titulo=API2&descripcion=probandooAPI
        nota_id = ID del cliente al que se le asignara la nota
♦ Buscar
    •Contactos
        URL.php?buscar_contacto_nombre=Nombre&buscar_contacto_apellido=Apellido&buscar_contacto_email=admin@gmail.com&buscar_contacto_telefono=1234567890
        Si se ingresa cualquiera de esos datos, arrojara las coincidencias encontradas
    •Contactos por ID
        URL.php?id=43141243
♦ Eliminar
    •Contactos
        carlosayala.cloud/API-Clientify/usuarios.php?eliminar_contacto_id=43141243

Este repositorio esta en constante mantenimiento.