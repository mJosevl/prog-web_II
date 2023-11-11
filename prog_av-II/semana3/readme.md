El programa implementado es para una tienda de lentes de prescripción. El objetivo es determinar el precio de venta final de los lentes en función del costo base del artículo, la marca y la fórmula recomendada.

La clase `Lente` tiene los siguientes atributos:
- `nombre`: El nombre del lente.
- `costo_base`: El costo base del lente antes de cualquier ajuste de precio.
- `marca`: La marca del lente, que podría influir en el precio final.
- `receta`: La prescripción médica para el lente, que también podría afectar el precio final.
- `costo_marca`: Un diccionario que almacena los costos adicionales asociados con cada marca de lente.
- `costo_receta`: Un diccionario que almacena los costos adicionales asociados con cada tipo de receta.

La clase `Lente` también tiene los siguientes métodos:
- `calcular_precio`: Este método calcula el precio final del lente. Primero, busca el costo adicional de la marca y la receta en los diccionarios `costo_marca` y `costo_receta`. Luego, multiplica el costo base del lente por estos costos adicionales para obtener el precio final. Finalmente, redondea el precio final a un decimal antes de devolverlo.
- `mostrar_detalles`: Este método imprime los detalles del lente, incluyendo el nombre, el costo base, la marca, la receta y el precio final.
- `__eq__`: Este es un método mágico que permite comparar dos lentes para ver si son iguales en términos de sus atributos. Si todos los atributos son iguales, devuelve `True`. De lo contrario, devuelve `False`.

Finalmente, se crean dos lentes: `lente_juan` y `lente_ana`, y se comparan usando el operador `==`. Si todos sus atributos son iguales, se imprime "Los lentes son iguales". De lo contrario, se imprime "Los lentes son diferentes". Luego, se muestran los detalles de `lente_juan` llamando al método `mostrar_detalles`. Esto imprimirá el nombre, el costo base, la marca, la receta y el precio final de `lente_juan`.