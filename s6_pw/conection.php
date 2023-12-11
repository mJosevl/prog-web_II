<?php
$servername = "localhost";
$username = "root";
$password = "root";

// Crear conexión
$conn = new mysqli($servername, $username, $password);

// Verificar conexión
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Seleccionar base de datos
mysqli_select_db($conn, 'Concesionario');

echo "Connected successfully";
?>
