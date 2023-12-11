<?php
function calcularPrecioTotal($precioBoleto, $cantidadAdultos, $cantidadNinos) {
    if($cantidadAdultos < 0 || $cantidadNinos < 0) {
        return "La cantidad de boletos debe ser un número mayor que cero";
    }
    $precioTotal = $precioBoleto * ($cantidadAdultos + 0.5 * $cantidadNinos);
    return $precioTotal;
}
?>


