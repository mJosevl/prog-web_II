import mysql.connector
from mysql.connector import Error

try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(host='localhost',
                                         database='biblioteca',
                                         user='root',
                                         password='admin')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE biblioteca")  # Crea la base de datos

        # Crea la tabla libros
        cursor.execute("CREATE TABLE libros (titulo VARCHAR(255), codigo VARCHAR(255), anio_publicacion INT, autor VARCHAR(255), editorial VARCHAR(255))")

        # Inserta 10 libros
        libros = [('Cuentos completos 1', '255218', 1990, 'Isaac Asimov', 'Penguin Random House'),
                  ('Cuentos completos 2', '255219', 1999, 'Isaac Asimov', 'Penguin Random House'),
                  ('Fundación', '001', 1951, 'Isaac Asimov', 'Gnome Press'),
                  ('Yo, robot', '002', 1950, 'Isaac Asimov', 'Gnome Press'),
                  ('Fundación e Imperio', '003', 1952, 'Isaac Asimov', 'Gnome Press'),
                  ('Segunda Fundación', '004', 1953, 'Isaac Asimov', 'Gnome Press'),
                  ('Bóvedas de acero', '005', 1953, 'Isaac Asimov', 'Doubleday'),
                  ('Los límites de la Fundación', '006', 1982, 'Isaac Asimov', 'Doubleday'),
                  ('Preludio a la Fundación', '007', 1988, 'Isaac Asimov', 'Doubleday'),
                  ('Fundación y Tierra', '008', 1986, 'Isaac Asimov', 'Doubleday')
                 ]
        cursor.executemany("INSERT INTO libros VALUES (%s, %s, %s, %s, %s)", libros)

        # Elimina los libros publicados antes del año 2000
        cursor.execute("DELETE FROM libros WHERE anio_publicacion < 2000")

        # Lista los libros publicados en el año actual
        from datetime import datetime
        current_year = datetime.now().year
        cursor.execute(f"SELECT * FROM libros WHERE anio_publicacion = {current_year}")
        result = cursor.fetchall()
        for row in result:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
