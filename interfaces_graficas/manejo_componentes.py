import tkinter as tk
from tkinter import ttk,messagebox

ventana = tk.Tk()
ventana.geometry('1400x600')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')



#variable para osociar al componente "textvariable=entrada_var1"
entrada_var1 = tk.StringVar(value='Valor por default')

entrada1 = ttk.Entry(ventana,width=40,justify=tk.CENTER,font=16, textvariable=entrada_var1)#
entrada1.grid(row=0,column=0,padx=20,pady=20)

etiqueta1 = ttk.Label(ventana,text=' Aqui agrego texto ')
etiqueta1.grid(row=1,column=0,columnspan=2)



def enviar():
    boton1.config(text=entrada_var1.get())
    entrada_var1.set('Cambio....')

    etiqueta1.config(text=entrada_var1.get())

    # mensajes
    messagebox.showinfo('Mensaje informativo')
    messagebox.showerror('hay un problema')
    messagebox.showwarning('Una alerta')

boton1= ttk.Button(ventana,text="Enviar", command=enviar)
boton1.grid(row=1,column=1,pady=20,padx=20,ipady=30,ipadx=30)

ventana.mainloop()