import tkinter as tk
from conexion import obtener_conexion

# Obtener la conexión a la base de datos
mydb = obtener_conexion()

# Crear un cursor para ejecutar comandos SQL
cursor = mydb.cursor()

class Farmaco:
    def __init__(self, nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.mg = mg
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento
        self.presentacion = presentacion

def enviar_datos():
    try:
        # Obtener los valores de los campos de texto
        nombre = nombre_entry.get()
        laboratorio = laboratorio_entry.get()
        mg = mg_entry.get()
        fecha_elaboracion = fecha_elaboracion_entry.get()
        fecha_vencimiento = fecha_vencimiento_entry.get()
        presentacion = presentacion_entry.get()


        # Crear la consulta SQL para la inserción
        sql_insert = "INSERT INTO Farmaco (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion) VALUES (%s, %s, %s, %s, %s, %s)"
        val_insert = (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion)

        # Ejecutar la consulta SQL de inserción
        cursor.execute(sql_insert, val_insert)

        # Hacer commit de la transacción
        mydb.commit()

        # Mostrar un mensaje de confirmación
        print(cursor.rowcount, "registro insertado.")

        # Limpiar los campos después de la inserción
        limpiar_campos()

        # Actualizar la lista de registros
        actualizar_lista()

    except Exception as e:
        # Manejar excepciones
        print(f"Error al insertar datos: {e}")

def limpiar_campos():
    # Limpiar los campos de texto
    nombre_entry.delete(0, tk.END)
    laboratorio_entry.delete(0, tk.END)
    mg_entry.delete(0, tk.END)
    fecha_elaboracion_entry.delete(0, tk.END)
    fecha_vencimiento_entry.delete(0, tk.END)
    presentacion_entry.delete(0, tk.END)

def actualizar_lista():
    # Limpiar la lista actual
    lista.delete(0, tk.END)

    # Obtener todos los registros de la base de datos
    cursor.execute("SELECT * FROM Farmaco")
    rows = cursor.fetchall()

    # Mostrar los registros en la lista
    for row in rows:
        lista.insert(tk.END, row)

def seleccionar_registro(event):
    # Obtener el índice del registro seleccionado en la lista
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        # Obtener el registro seleccionado
        registro = lista.get(indice)
        # Mostrar los datos en los campos de texto
        nombre_entry.delete(0, tk.END)
        nombre_entry.insert(tk.END, registro[1])
        laboratorio_entry.delete(0, tk.END)
        laboratorio_entry.insert(tk.END, registro[2])
        mg_entry.delete(0, tk.END)
        mg_entry.insert(tk.END, registro[3])
        fecha_elaboracion_entry.delete(0, tk.END)
        fecha_elaboracion_entry.insert(tk.END, registro[4])
        fecha_vencimiento_entry.delete(0, tk.END)
        fecha_vencimiento_entry.insert(tk.END, registro[5])
        presentacion_entry.delete(0, tk.END)
        presentacion_entry.insert(tk.END, registro[6])

def actualizar_registro():
    try:
        # Obtener el índice del registro seleccionado en la lista
        seleccion = lista.curselection()
        if seleccion:
            indice = seleccion[0]
            # Obtener el registro seleccionado
            registro = lista.get(indice)

            # Obtener los nuevos valores de los campos de texto
            nombre = nombre_entry.get()
            laboratorio = laboratorio_entry.get()
            mg = mg_entry.get()
            fecha_elaboracion = fecha_elaboracion_entry.get()
            fecha_vencimiento = fecha_vencimiento_entry.get()
            presentacion = presentacion_entry.get()

            # Crear la consulta SQL para la actualización
            sql_update = "UPDATE Farmaco SET nombre=%s, laboratorio=%s, mg=%s, fecha_elaboracion=%s, fecha_vencimiento=%s, presentacion=%s WHERE id=%s"
            val_update = (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion, registro[0])

            # Ejecutar la consulta SQL de actualización
            cursor.execute(sql_update, val_update)

            # Hacer commit de la transacción
            mydb.commit()

            # Limpiar los campos después de la actualización
            limpiar_campos()

            # Actualizar la lista de registros
            actualizar_lista()

            # Mostrar un mensaje de confirmación
            print(cursor.rowcount, "registro(s) actualizado(s).")

    except Exception as e:
        # Manejar excepciones
        print(f"Error al actualizar datos: {e}")

def eliminar_registro():
    try:
        # Obtener el índice del registro seleccionado en la lista
        seleccion = lista.curselection()
        if seleccion:
            indice = seleccion[0]
            # Obtener el registro seleccionado
            registro = lista.get(indice)

            # Crear la consulta SQL para la eliminación
            sql_delete = "DELETE FROM Farmaco WHERE id=%s"
            val_delete = (registro[0],)

            # Ejecutar la consulta SQL de eliminación
            cursor.execute(sql_delete, val_delete)

            # Hacer commit de la transacción
            mydb.commit()

            # Limpiar los campos después de la eliminación
            limpiar_campos()

            # Actualizar la lista de registros
            actualizar_lista()

            # Mostrar un mensaje de confirmación
            print(cursor.rowcount, "registro(s) eliminado(s).")

    except Exception as e:
        # Manejar excepciones
        print(f"Error al eliminar datos: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario Farmacia")

# Crear el título del formulario
titulo = tk.Label(ventana, text="Formulario de Farmacia", font=("Arial", 24))
titulo.pack()

# Crear los widgets
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)
nombre_label.pack(anchor='w')
nombre_entry.pack()

laboratorio_label = tk.Label(ventana, text="Laboratorio:")
laboratorio_entry = tk.Entry(ventana)
laboratorio_label.pack(anchor='w')
laboratorio_entry.pack()

mg_label = tk.Label(ventana, text="mg:")
mg_entry = tk.Entry(ventana)
mg_label.pack(anchor='w')
mg_entry.pack()

fecha_elaboracion_label = tk.Label(ventana, text="Fecha de elaboración:")
fecha_elaboracion_entry = tk.Entry(ventana)
fecha_elaboracion_label.pack(anchor='w')
fecha_elaboracion_entry.pack()

fecha_vencimiento_label = tk.Label(ventana, text="Fecha de vencimiento:")
fecha_vencimiento_entry = tk.Entry(ventana)
fecha_vencimiento_label.pack(anchor='w')
fecha_vencimiento_entry.pack()

presentacion_label = tk.Label(ventana, text="Presentación:")
presentacion_entry = tk.Entry(ventana)
presentacion_label.pack(anchor='w')
presentacion_entry.pack()

# Crear el botón de enviar
enviar_button = tk.Button(ventana, text="Enviar", command=enviar_datos)
enviar_button.pack()

# Crear el botón de actualizar
actualizar_button = tk.Button(ventana, text="Actualizar", command=actualizar_registro)
actualizar_button.pack()

# Crear el botón de eliminar
eliminar_button = tk.Button(ventana, text="Eliminar", command=eliminar_registro)
eliminar_button.pack()

# Crear la lista para mostrar los registros
lista = tk.Listbox(ventana, height=10, width=50)
lista.pack()

# Asociar la función de selección con un evento de clic en la lista
lista.bind('<<ListboxSelect>>', seleccionar_registro)

# Actualizar la lista de registros al iniciar la aplicación
actualizar_lista()

# Iniciar el bucle principal
ventana.mainloop()
