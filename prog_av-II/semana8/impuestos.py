from tkinter import *
import csv

def calculo():
    try:
        ingreso = float(ingreso_e.get())
        impuesto = ingreso * 0.20
        mensaje_resultado.set(f"El impuesto a pagar es: {round(impuesto, 2)}")
    except ValueError:
        mensaje_resultado.set("Error: Ingreso no válido")

def guardar():
    try:
        with open('impuestos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            ingreso = float(ingreso_e.get())
            impuesto = ingreso * 0.20
            mensaje = f"El impuesto a pagar es: {round(impuesto, 2)}"
            mensaje_resultado.set(mensaje)
            writer.writerow([nombre_e.get(), apellido_e.get(), rut_e.get(), sexo_e.get(), ingreso, round(impuesto, 2)])
    except Exception as e:
        mensaje_resultado.set(f"Error al guardar: {e}")

ventana = Tk()
ventana.title('Formulario de Impuestos')
ventana.geometry('500x400')

# Etiquetas
Label(ventana, text="Nombre:").place(x=50, y=50)
Label(ventana, text="Apellido:").place(x=50, y=100)
Label(ventana, text="RUT:").place(x=50, y=150)
Label(ventana, text="Sexo:").place(x=50, y=200)
Label(ventana, text="Ingreso:").place(x=50, y=250)

# Campos de entrada con fondo verde agua
nombre_e = Entry(ventana, bg='aquamarine')
nombre_e.place(x=200, y=50)
apellido_e = Entry(ventana, bg='aquamarine')
apellido_e.place(x=200, y=100)
rut_e = Entry(ventana, bg='aquamarine')
rut_e.place(x=200, y=150)
sexo_e = Entry(ventana, bg='aquamarine')
sexo_e.place(x=200, y=200)
ingreso_e = Entry(ventana, bg='aquamarine')
ingreso_e.place(x=200, y=250)

# Variable para mostrar el impuesto calculado y mensaje
mensaje_resultado = StringVar()
mensaje_resultado.set("El impuesto a pagar:")
resultado_label = Label(ventana, textvariable=mensaje_resultado)
resultado_label.place(x=50, y=300)

# Botones
calcular_b = Button(ventana, text="Calcular", command=calculo)
calcular_b.place(x=200, y=350)
guardar_b = Button(ventana, text="Guardar", command=guardar)
guardar_b.place(x=300, y=350)

ventana.mainloop()
