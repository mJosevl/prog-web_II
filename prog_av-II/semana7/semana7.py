

import matplotlib.pyplot as plt
import numpy as np

escalafon = ['Instructor', 'Asistente', 'Agregado', 'Asociado']
casos = [945, 698, 736, 590]

plt.bar(escalafon, casos, color='blue')
plt.xlabel('Escalafón')
plt.ylabel('Casos')
plt.title('Clasificación de Profesores')
plt.show()

# Series de datos adicionales
serie1 = np.random.normal(750, 50, 700)
serie2 = np.random.normal(900, 20, 700)
serie3 = np.random.normal(500, 40, 700)

# Boxplot para las series 1, 2, 3
plt.boxplot([serie1, serie2, serie3], labels=['Serie 1', 'Serie 2', 'Serie 3'])
plt.xlabel('Series')
plt.ylabel('Valores')
plt.title('Boxplot de Series de Datos')
plt.show()

# Series de datos adicionales
serie1 = np.random.normal(750, 50, 700)
serie2 = np.random.normal(900, 20, 700)
serie3 = np.random.normal(500, 40, 700)

# Boxplot para las series 1, 2, 3
plt.boxplot([serie1, serie2, serie3], labels=['Serie 1', 'Serie 2', 'Serie 3'])
plt.xlabel('Series')
plt.ylabel('Valores')
plt.title('Boxplot de Series de Datos')
plt.show()

x = range(200)
y = range(200) + np.random.randint(0, 20, 200)

plt.scatter(x, y, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagrama de Dispersión')
plt.show()
