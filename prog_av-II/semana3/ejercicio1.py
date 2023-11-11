class Personal:
    def __init__(self, nombre, sueldo, cargo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.cargo = cargo

    def metodo_pago(self):
        if self.cargo == 'Gerente':
            return self.pago_gerente()
        elif self.cargo == 'Empleado':
            return self.pago_empleado()
        else:
            return "Cargo no reconocido"

    def pago_gerente(self):
        # Implementar lógica de pago para gerente
        return "Pago para gerente"

    def pago_empleado(self):
        # Implementar lógica de pago para empleado
        return "Pago para empleado"

juan = Personal('Juan', 5000, 'Gerente')
print(juan.pago_gerente())
print(juan.nombre)
print(juan.sueldo)


