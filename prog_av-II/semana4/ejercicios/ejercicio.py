from tkinter import*

# Crear la ventana principal
ventana = Tk()
ventana.title("Mi primera GUI con Tkinter")

# Crear un botón que salude al usuario
def saludar():
    print("¡Hola, usuario!")

boton = Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
