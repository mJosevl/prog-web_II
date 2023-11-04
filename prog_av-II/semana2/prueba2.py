class servivo():
    def __init__(self, edad, nombre, sexo, peso, tipo):
        self.edad=edad
        self.nombre=nombre
        self.sexo=sexo
        self.peso=peso
        self.tipo=tipo
class perro(servivo):
    def patas(self):
        mensaje='Posee 4 patas'
        return mensaje
class persona(servivo):
    def piernas(self):
        mensaje='Posee 2 piernas'
        return mensaje
objeto1=perro(2,'Sparky', 'Masculino', 10, 'canino')
objeto2=persona(45,'Jose', 'Masculino', 76, 'Humano')
print('El primer objeto tiene las siguientes caracteristicas : ')
print('Nombre : ' , objeto1.nombre, 'Edad : ' , objeto1.edad , 'Sexo : ', objeto1.sexo)
print('Peso: ' , objeto1.peso , 'Tipo: ' , objeto1.tipo, 'Particularidad : ', objeto1.patas())
print('El segundo objeto tiene las siguientes caracteristicas : ')
print('Nombre : ' , objeto2.nombre, 'Edad : ' , objeto2.edad , 'Sexo : ', objeto2.sexo)
print('Peso: ' , objeto2.peso , 'Tipo: ' , objeto2.tipo, 'Particularidad : ', objeto2.piernas())