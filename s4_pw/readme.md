 Línea por línea de la función `calcularCuota`:

```javascript
function calcularCuota() {
```
Esta línea define una nueva función llamada `calcularCuota`.

```javascript
    var edad = document.getElementById('edad').value;
```
Esta línea obtiene el valor del elemento HTML con el id 'edad'. Este valor se guarda en la variable `edad`.

```javascript
    var esSocio = document.getElementById('esSocio').checked;
```
Esta línea verifica si el checkbox con el id 'esSocio' está marcado (es decir, si los padres son socios). El resultado (verdadero o falso) se guarda en la variable `esSocio`.

```javascript
    var cuota = 800;
```
Esta línea establece el valor inicial de la cuota en 800.

```javascript
    if (edad > 60) {
        cuota *= 0.6;
    }
```
Si la edad es mayor a 60, se aplica un descuento del 40% a la cuota (es decir, se multiplica la cuota por 0.6).

```javascript
    else if (edad < 21) {
        cuota *= esSocio ? 0.65 : 0.75;
    }
```
Si la edad es menor a 21, se aplica un descuento a la cuota. Si los padres son socios (es decir, `esSocio` es verdadero), el descuento es del 35% (la cuota se multiplica por 0.65). Si los padres no son socios, el descuento es del 25% (la cuota se multiplica por 0.75).

```javascript
    document.getElementById('resultado').innerText = 'La cuota es: ' + cuota;
}
```
Finalmente, se muestra el resultado en el elemento HTML con el id 'resultado'.
