class Libros():
    def __init__(self, nombre, autor, cota, genero, editorial, _fecha_edicion, pais_edicion):
        self.nombre = nombre
        self.autor = autor
        self.cota = cota
        self.genero = genero
        self.editorial = editorial
        self._fecha_edicion = _fecha_edicion
        self.pais_edicion = pais_edicion

    def Libro(self):
        print('Nombre: ', self.nombre, 'Autor: ', self.autor, 'Cota: ', self.cota, 'Género: ', self.genero,
              'Editorial: ', self.editorial, 'País de edición: ', self.pais_edicion)

libro1 = Libros('Fundación', 'Isaac Asimov', 'Fundacion', 'Ciencia Ficción', 'Cenit', '1951', 'EEUU')
libro2 = Libros('Fundación e Imperio', 'Isaac Asimov', 'Fundacion e Imperio', 'Ciencia Ficción', 'Cenit', '1952', 'EEUU')
libro3 = Libros('El Gran Gatsby', 'F. Scott Fitzgerald', 'Gatsby', 'Ficción', 'Scribner', '1925', 'EEUU')
libro4 = Libros('1984', 'George Orwell', '1984', 'Ciencia Ficción', 'Secker & Warburg', '1949', 'Reino Unido')
libro5 = Libros('El Código Da Vinci', 'Dan Brown', 'Da Vinci', 'Misterio', 'Doubleday', '2003', 'EEUU')

libro1.Libro()
libro2.Libro()
libro3.Libro()
libro4.Libro()
libro5.Libro()
