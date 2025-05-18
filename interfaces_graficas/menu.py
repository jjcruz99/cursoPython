import sys
import tkinter as tk
from tkinter import ttk, messagebox , Menu


ventana = tk.Tk()
ventana.geometry('1000x700')
ventana.title('Nueva ventana')
ventana.iconbitmap('icono.ico')


def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento click')

def salir():
    ventana.quit()
    ventana.destroy()
    print('Fin de la aplicacion...')
    sys.exit()

def crear_menu():
    #configurar el menu Principal
    menu_principal = Menu(ventana)
    submenu_archivo = Menu(menu_principal, tearoff=0)

    #crear los submenus
    submenu_archivo.add_command(label='Nuevo')
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label='Salir',command=salir) ##command llama al metodo salir

    submenu_ayuda= Menu(menu_principal,tearoff=0)
    submenu_ayuda.add_command(label='Acerca de')

    #agregar el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label ='Archivo')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    ventana.config(menu = menu_principal)

# Crear boton en la ventana
boton1 = ttk.Button(ventana, text='Click', command=evento_click)

# desplegar boton
boton1.pack()

crear_menu()

# Ejecutar al final
ventana.mainloop()