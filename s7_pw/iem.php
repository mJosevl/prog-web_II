<?php
class Estudiante {
    private $nombre;
    private $apellido;
    private $id;
    private $materias = array();

    function __construct($nombre, $apellido, $id) {
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->id = $id;
    }

    function getNombre() {
        return $this->nombre;
    }

    function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    function getApellido() {
        return $this->apellido;
    }

    function setApellido($apellido) {
        $this->apellido = $apellido;
    }

    function getId() {
        return $this->id;
    }

    function setId($id) {
        $this->id = $id;
    }

    function getMaterias() {
        return $this->materias;
    }

    function addMateria($materia) {
        array_push($this->materias, $materia);
    }

    function removeMateria($materia) {
        if (($key = array_search($materia, $this->materias)) !== false) {
            unset($this->materias[$key]);
        }
    }
}

class Materia {
    private $nombre;
    private $id;
    private $notas = array();

    function __construct($nombre, $id) {
        $this->nombre = $nombre;
        $this->id = $id;
    }

    function getNombre() {
        return $this->nombre;
    }

    function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    function getId() {
        return $this->id;
    }

    function setId($id) {
        $this->id = $id;
    }

    function getNotas() {
        return $this->notas;
    }

    function addNota($nota) {
        array_push($this->notas, $nota);
    }

    function removeNota($nota) {
        if (($key = array_search($nota, $this->notas)) !== false) {
            unset($this->notas[$key]);
        }
    }
}

class Nota {
    private $valor;
    private $id;

    function __construct($valor, $id) {
        $this->valor = $valor;
        $this->id = $id;
    }

    function getValor() {
        return $this->valor;
    }

    function setValor($valor) {
        $this->valor = $valor;
    }

    function getId() {
        return $this->id;
    }

    function setId($id) {
        $this->id = $id;
    }
}

$estudiante1 = new Estudiante("Juan", "Perez", "1");
$estudiante2 = new Estudiante("Maria", "Gomez", "2");

$materia1 = new Materia("Matematicas", "1");
$materia2 = new Materia("Fisica", "2");

$nota1 = new Nota("10", "1");
$nota2 = new Nota("8", "2");
?>
