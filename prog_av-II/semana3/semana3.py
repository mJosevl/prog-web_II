class Lente:
    def __init__(self, nombre, costo_base, marca, receta):
        self.nombre = nombre
        self.costo_base = costo_base
        self.marca = marca
        self.receta = receta

        # Diccionario de costos por marca
        self.costo_marca = {
            'MarcaX': 1.2,
            'MarcaY': 1.3,
            
        }

        # Diccionario de costos por receta
        self.costo_receta = {
            'RecetaA': 1.1,
            'RecetaB': 1.2,
         
        }

    def calcular_precio(self):
        # Obtiene el costo de la marca y la receta del lente
        costo_marca = self.costo_marca.get(self.marca, 1)
        costo_receta = self.costo_receta.get(self.receta, 1)

        # Calcula el precio final
        precio_final = self.costo_base * costo_marca * costo_receta

        # Redondea el precio final a un decimal
        precio_final = round(precio_final, 1)

        return precio_final

    def mostrar_detalles(self):
        print(f'Nombre: {self.nombre}')
        print(f'Costo Base: {self.costo_base}')
        print(f'Marca: {self.marca}')
        print(f'Receta: {self.receta}')
        print(f'Precio Final: {self.calcular_precio()}')
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.costo_base == otro.costo_base and self.marca == otro.marca and self.receta == otro.receta

# Crear una instancia de la clase Lente
lente_juan = Lente('Juan', 5000, 'MarcaX', 'RecetaA')
lente_ana = Lente('Ana', 5000, 'MarcaX', 'RecetaA')
if lente_juan == lente_ana:
        print("Los lentes son iguales")
else:
        print("Los lentes son diferentes")
# Mostrar los detalles del lente
lente_juan.mostrar_detalles()

