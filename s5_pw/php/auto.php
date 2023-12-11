<?php
class Auto {
    private $matricula;
    private $marca;
    private $modelo;
    private $ano;
    private $color;

    public function setMatricula($matricula) { $this->matricula = $matricula; }
    public function setMarca($marca) { $this->marca = $marca; }
    public function setModelo($modelo) { $this->modelo = $modelo; }
    public function setAno($ano) { $this->ano = $ano; }
    public function setColor($color) { $this->color = $color; }

    public function getMatricula() { return $this->matricula; }
    public function getMarca() { return $this->marca; }
    public function getModelo() { return $this->modelo; }
    public function getAno() { return $this->ano; }
    public function getColor() { return $this->color; }
}

$auto = new Auto();
$auto->setMatricula($_POST["matricula"]);
$auto->setMarca($_POST["marca"]);
$auto->setModelo($_POST["modelo"]);
$auto->setAno($_POST["ano"]);
$auto->setColor($_POST["color"]);

echo "Matrícula: " . $auto->getMatricula() . "<br>";
echo "Marca: " . $auto->getMarca() . "<br>";
echo "Modelo: " . $auto->getModelo() . "<br>";
echo "Año: " . $auto->getAno() . "<br>";
echo "Color: " . $auto->getColor() . "<br>";
?>
