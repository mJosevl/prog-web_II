# Sistema de Registro y Control de Calificaciones

Este sistema fue desarrollado utilizando Programación Orientada a Objetos (POO) y PHP. Su objetivo es el registro y control de las calificaciones obtenidas por los estudiantes de un instituto de educación media.

## Clases y Objetos

El sistema consta de tres clases principales: `Estudiante`, `Materia` y `Nota`.

### Clase Estudiante

La clase `Estudiante` representa a un estudiante en el instituto. Cada estudiante tiene un nombre, un apellido y un ID único. Además, cada estudiante tiene una lista de materias que está cursando.

Un objeto de la clase `Estudiante` sería un estudiante específico en el instituto.

### Clase Materia

La clase `Materia` representa una materia que un estudiante puede cursar. Cada materia tiene un nombre y un ID único. Además, cada materia tiene una lista de notas que los estudiantes han obtenido en esa materia.

Un objeto de la clase `Materia` sería una materia específica que los estudiantes pueden cursar.

### Clase Nota

La clase `Nota` representa una nota que un estudiante ha obtenido en una materia. Cada nota tiene un valor y un ID único.

Un objeto de la clase `Nota` sería una nota específica que un estudiante ha obtenido en una materia.

## Componentes de las Clases

Cada clase tiene varios componentes, incluyendo atributos y métodos.

Por ejemplo, la clase `Estudiante` tiene los siguientes componentes:

- Atributos: nombre, apellido, id, materias (un array de objetos de la clase Materia).
- Métodos: getNombre(), setNombre(), getApellido(), setApellido(), getId(), setId(), getMaterias(), addMateria(), removeMateria().

Estos componentes permiten obtener y modificar los datos de un estudiante, así como gestionar las materias que está cursando.

## Definición de las Clases en PHP

Las clases se definen en PHP utilizando la palabra clave `class`, seguida del nombre de la clase y un conjunto de llaves `{}` que contienen los atributos y métodos de la clase.

Cada clase tiene un constructor, que es un método especial que se llama automáticamente cuando se crea un objeto de la clase. El constructor se utiliza para inicializar los atributos del objeto.

Además, cada clase tiene métodos `get` y `set` para cada atributo, que permiten obtener y modificar los valores de los atributos, respectivamente.

Finalmente, se crean dos objetos para cada clase utilizando la palabra clave `new`, seguida del nombre de la clase y un conjunto de paréntesis `()` que contienen los argumentos para el constructor de la clase.
