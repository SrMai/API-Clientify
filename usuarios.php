<?php
 /*****************************************************************
 * 																  *
 *   	   Copyright (c) 2023 Carlos Adrian Ayala Gonzalez		  *
 *  					All rights reserved.					  *
 *																  *
 *		Github: SrMai | srmai.github.io | carlosayala.cloud		  *
 * 													              *
 * ***************************************************************/
/* API REST para clientify */
	header("Content-Type: application/json");
	include 'class-usuario.php';
	include 'routes.php';
	switch($_SERVER['REQUEST_METHOD']){
		case 'POST':
			echo "ERROR 500";
			break;
		case 'GET':
		if(isset($_GET['id'])){
			Usuario::obtenerUsuario($_GET['id']);
			$resultado["mensaje"] = "Retornar el contacto con el id: " . $_GET['id'];
			echo json_encode($resultado);
		}elseif(isset($_GET['nota_id']) && isset($_GET['titulo']) && isset($_GET['descripcion'])){
			Usuario::guardarNota($token, $_GET['nota_id'], $_GET['titulo'], $_GET['descripcion'], $CrearNota);
		}elseif(isset($_GET['eliminar_contacto_id'])){
			Usuario::eliminarContacto($token, $_GET['eliminar_contacto_id'], $EliminarContacto);
		}elseif(isset($_GET['crear_contacto_nombre']) && isset($_GET['crear_contacto_apellido']) && isset($_GET['crear_contacto_email']) && isset($_GET['crear_contacto_telefono'])){
			Usuario::crearContacto($token, $_GET['crear_contacto_nombre'], $_GET['crear_contacto_apellido'], $_GET['crear_contacto_email'], $_GET['crear_contacto_telefono'], $CrearContacto);
		}elseif(isset($_GET['buscar_contacto_nombre']) || isset($_GET['buscar_contacto_apellido']) || isset($_GET['buscar_contacto_email']) || isset($_GET['buscar_contacto_telefono'])){
			$variables = $token . " " . $_GET['buscar_contacto_nombre'] . " " . $_GET['buscar_contacto_apellido'] . " " . $_GET['buscar_contacto_email'] . " " . $_GET['buscar_contacto_telefono'];
			Usuario::buscarContacto($variables, $BuscarContacto);
		}else{
			Usuario::obtenerUsuarios();
			$resultado["mensaje"] = "Retornar todos los contactos";
			echo json_encode($resultado);
		}
			break;
		case 'PUT':
			$_PUT = json_decode(file_get_contents('php://input'), true);
			echo "ERROR 500";
			break;
		case 'DELETE':
			echo "ERROR 500";
			break;
	}
?>