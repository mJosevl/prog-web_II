import pandas as pd

# Crear un conjunto de datos con las variables requeridas
data = {
    'nombre': ['Juan', 'Pedro', 'María', 'Ana'],
    'apellido': ['Pérez', 'González', 'García', 'López'],
    'RUT': ['11.111.111-1', '22.222.222-2', '33.333.333-3', '44.444.444-4'],
    'sexo': ['M', 'M', 'F', 'F'],
    'dirección': ['Calle 1', 'Calle 2', 'Calle 3', 'Calle 4'],
    'edad': [30, 40, 25, 35]
}

df = pd.DataFrame(data)
# Dividir el conjunto de datos en dos subconjuntos
df_masculino = df[df['sexo'] == 'M']
df_femenino = df[df['sexo'] == 'F']
# Consolidar los dos subconjuntos de datos en un solo conjunto
df_consolidado = pd.concat([df_masculino, df_femenino])

print(df_consolidado)