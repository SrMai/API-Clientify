<?php

 /*****************************************************************
 * 																  *
 *   	   Copyright (c) 2023 Carlos Adrian Ayala Gonzalez		  *
 *  					All rights reserved.					  *
 *																  *
 *		Github: SrMai | carlosayala.cloud | srmai.github.io		  *
 * 													              *
 * ***************************************************************/

class Usuario{
	/**Notas*/
	 public function guardarNota($token, $id, $title, $description, $accion)
	 {
		/**Modo de uso:
		 * Token = token API
		 * id = id del usuario
		 * title = titulo de la nota
		 * description = descripcion de la nota
		 * accion = ruta del script
		 */
		$variables = $token . " " . $id . " " . $title . " " . $description;
		$output = shell_exec("$accion $variables");
		echo "Se creo la siguiente nota: ".$output;
	 }

	 /**Contactos */
	 public function eliminarContacto($token, $id, $accion)
	 {
		/**Modo de uso:
		 * Token = token API
		 * id = id del contacto
		 * accion = ruta del script
		 */
		$variables = $token . " " . $id;
		$output = shell_exec("$accion $variables");
		echo $output;
	 }
	 
	 public static function obtenerUsuarios()
	 {
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, 'https://api.clientify.net/v1/contacts/');
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
		$headers = array();
		$headers[] = 'Authorization: Token b02655bd6a3d03900958f1d8b53231098a880a81';
		curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

		$result = curl_exec($ch);
		if (curl_errno($ch)) {
		    echo 'Error:' . curl_error($ch);
		}
		echo $result;
		curl_close($ch);
	 }

	 public static function obtenerUsuario($indice)
	 {
		$ch = curl_init();
		var_dump($indice);
		curl_setopt($ch, CURLOPT_URL, 'https://api.clientify.net/v1/contacts/'.$indice.'/');
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
		$headers = array();
		$headers[] = 'Authorization: Token b02655bd6a3d03900958f1d8b53231098a880a81';
		curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

		$result = curl_exec($ch);
		if (curl_errno($ch)) {
		    echo 'Error:' . curl_error($ch);
		}
		echo $result;
		curl_close($ch);
	 }
}

?>