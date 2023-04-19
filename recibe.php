<?php
// Verifica si se ha enviado una solicitud POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recibe los datos enviados por la solicitud POST
    $data = json_decode(file_get_contents('php://input'), true);

    // Si los datos son válidos, los guarda en un archivo de texto
    if (!empty($data)) {
        $file = 'datos.txt';
        $current = file_get_contents($file);
        $current .= print_r($data, true);
        file_put_contents($file, $current);
        echo "Los datos se han guardado correctamente en el archivo 'datos.txt'";
    } else {
        echo "No se han recibido datos válidos.";
    }
} else {
    echo "Este archivo solo acepta solicitudes POST.";
}
?>
