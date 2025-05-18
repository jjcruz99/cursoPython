
import tkinter as tk
from tkinter import ttk , messagebox , Menu
from login.usuario import Usuario

ventana = tk.Tk()
ventana.geometry('300x200')
ventana.title('Login')
ventana.resizable(0,0)


#configurar grid
#se define una relacion de 1 a 3 = columna0=25% y columna1=75%
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)


etiqueta1 = ttk.Label(ventana,text='Usuario',font=12,width=7) #with define el ancho para 7 caracteres
etiqueta1.grid(row=0,column=0,padx=5,pady=5,sticky=tk.E)
entrada1 = ttk.Entry(ventana,font=12)
entrada1.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)

etiqueta2 = ttk.Label(ventana,text='Clave',font=12)
etiqueta2.grid(row=1,column=0,padx=5,pady=5,sticky=tk.E)
entrada2 = ttk.Entry(ventana,justify=tk.LEFT,font=12,show='*')
entrada2.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def login():
    messagebox.showinfo('Datos Login',
                        f'Usiario {entrada1.get()} , Clave {entrada2.get()}')

botton1 = tk.Button(ventana,text='Login',background='blue',font=12,justify=tk.CENTER,command=login)
botton1.grid(row=2,column=0,padx=5,pady=5,ipady=1,ipadx=1,columnspan=2)#columnspan=2 y justify=tk.CENTER toma dos columnas y se ubica en el centro


ventana.mainloop()
