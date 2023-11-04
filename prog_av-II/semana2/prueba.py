class persona():
    def __init__(self, __edad, nombre, sexo, peso):
        self.edad=__edad
        self.nombre=nombre
        self.sexo=sexo
        self.peso=peso

    def presenta(self):
        print('Hola ' , 'me llamo ' , self.nombre , 'un placer saludarte')
    def correr(self):
        print('En estos momentos ', self.nombre , 'se encuentra corriendo')
persona1=persona(32,'Carlos', 'Masculino', 78.9)
persona2=persona(23,'Maria', 'Femenino', 65.4)
persona1.edad

