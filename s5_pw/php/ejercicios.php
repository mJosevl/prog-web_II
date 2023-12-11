<?php
function contarDivisiblesPorSiete() {
    $contador = 0;
    for($i = 1; $i <= 50; $i++) {
        if($i % 7 == 0) {
            $contador++;
        }
    }
    return $contador;
}
?>