import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('900x600')
ventana.title('Manejo de GRID')
ventana.iconbitmap('icono.ico')

#metodos de los eventos
def evento1():
    boton1.config(text='Presionado boton')

def evento2():
    boton2.config(text='Presionadooo boton')

def evento4():
    boton4.config(text='Presionado', fg='blue',relief=tk.GROOVE,bg='red')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=10)

boton1 = ttk.Button(ventana, text='Botton 1', command=evento1)
boton1.grid(row=0, column=0,sticky='NSEW',padx=40,pady=30,ipadx=20,ipady=20,columnspan=2,rowspan=2)

boton2 = ttk.Button(ventana, text='Botton 2', command=evento2)
boton2.grid(row=0, column=2,sticky='NSEW',padx=20,pady=40)

boton3 = ttk.Button(ventana, text='Botton 3', command=evento1)
boton3.grid(row=2, column=0,sticky='NSWE',padx=20,pady=40)

boton4 = tk.Button(ventana, text='Botton 4', command=evento4,background='blue')
boton4.grid(row=2, column=1,sticky='NSEW',padx=20,pady=40)


ventana.mainloop()