<?php
// Insertar auto
$sql = "INSERT INTO Autos (matricula, marca, modelo, anno, color) VALUES ('" . $_POST["matricula"] . "','" . $_POST["marca"] . "','" . $_POST["modelo"] . "'," . $_POST["anno"] . ",'" . $_POST["color"] . "')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Consultar autos
$sql = "SELECT matricula, marca, modelo, anno, color FROM Autos";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "matricula: " . $row["matricula"] . " - Marca: " . $row["marca"] . " - Modelo: " . $row["modelo"] . " - Año: " . $row["anno"] . " - Color: " . $row["color"] . "<br>";
    }
} else {
    echo "0 results";
}

// Modificar auto
$sql = "UPDATE Autos SET marca='Ford' WHERE matricula='ABC123'";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

// Eliminar auto
$sql = "DELETE FROM Autos WHERE matricula='ABC123'";

if ($conn->query($sql) === TRUE) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . $conn->error;
}

$conn->close();
