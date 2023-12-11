from tkinter import Tk, Label, Entry, Button

def envio():
    nombre1 = nombre_e.get()
    apell1 = apell_e.get()
    rut1 = rut_e.get()
    dire1 = dire_e.get()
    print('Los datos introducidos son : ', nombre1 , apell1, ' ' , dire1 , ' ' , rut1)

ventana = Tk()
ventana.geometry('650x550')
ventana.title('Formulario de registro de datos')
ventana.resizable(False, False)
ventana.config(background= 'Yellow')

principal_label = Label(text='Datos personales', font=('Cambria', 14, 'bold'), bg='Blue', justify= 'center', fg='White', width=70, height=1)
principal_label.place(x=0, y=0)

nombre_t = Label(text='Nombre', font=('Cambria', 14, 'bold'), justify= 'left', bg='Yellow', fg='Black')
nombre_t.place(x=0,y=100)
nombre_e = Entry(ventana)
nombre_e.place(x=200, y=100)

apell_t = Label(text='Apellido', font=('Cambria', 14, 'bold'), justify= 'left', bg='Yellow', fg='Black')
apell_t.place(x=0,y=150)
apell_e = Entry(ventana)
apell_e.place(x=200, y=150)

rut_t = Label(text='RUT', font=('Cambria', 14, 'bold'), justify= 'left', bg='Yellow', fg='Black')
rut_t.place(x=0,y=200)
rut_e = Entry(ventana)
rut_e.place(x=200, y=200)

dire_t = Label(text='Dirección', font=('Cambria', 14, 'bold'), justify= 'left', bg='Yellow', fg='Black')
dire_t.place(x=0,y=250)
dire_e = Entry(ventana)
dire_e.place(x=200, y=250)

submit_button = Button(ventana, text="Submit", command=envio)
submit_button.place(x=200, y=300)

ventana.mainloop()
