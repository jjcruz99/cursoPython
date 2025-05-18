# GUI - Graphical User Interface
# Tkinter - TK Interface
#

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
#Modificar el tamaño de la ventana
ventana.geometry('1000x700')
ventana.title('Nueva ventana')
ventana.iconbitmap('icono.ico')

def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento click')
    
    #crear otro componente
    boton2 = ttk.Button(ventana,text='Otro')
    boton2.pack()

#Crear boton en la ventana
boton1 = ttk.Button(ventana,text='Click',command=evento_click)

#desplegar boton
boton1.pack()

# Ejecutar al final
ventana.mainloop()