# Diccionario para almacenar los datos
datos = {
    "Ballena": [150000, 150500, 151000, 151500, 152000, 152500],  # pesos en kg
    "Perro": [10, 10.5, 11, 11.5, 12, 12.5],  # pesos en kg
    "Jirafa": [800, 810, 820, 830, 840, 850],  # pesos en kg
    "Avestruz": [100, 105, 110, 115, 120, 125],  # pesos en kg
}

# Función para calcular el promedio
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Imprimir los datos
for especie, pesos in datos.items():
    promedio = calcular_promedio(pesos)
    print(f"La especie {especie} tiene los siguientes pesos registrados en los últimos 6 meses: {pesos} con un peso promedio de {promedio:.2f} kg.")
