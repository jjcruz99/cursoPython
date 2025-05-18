import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1400x600')
ventana.title('Manejo de GRID')
ventana.iconbitmap('icono.ico')


entrada1 = ttk.Entry(ventana,width=40,justify=tk.CENTER,font=16)
entrada1.grid(row=0,column=0,padx=20,pady=20)
entrada1.insert(0,'Digite una cadena')
entrada1.insert(tk.END, '-')

entrada2 = ttk.Entry(ventana,width=40,justify=tk.CENTER,font=16,show='*')
entrada2.grid(row=0,column=1,padx=20,pady=20)


entrada3 = ttk.Entry(ventana,width=40,justify=tk.CENTER,font=16)
entrada3.grid(row=1,column=0,padx=20,pady=20)
#entrada3.config(state=tk.DISABLED)

def enviar():
    print(entrada1.get())

    #capturar el texto y pasarlo a la entrada 3
    entrada3.insert(0,entrada1.get())

    #Seleccionar todo el texto de la caja
    entrada1.select_range(0,tk.END)
    entrada1.focus()

    #Borrar todo el cotenido de la pantalla
    #entrada1.delete(0,tk.END)

boton1= ttk.Button(ventana,text="Enviar", command=enviar)
boton1.grid(row=1,column=1)

ventana.mainloop()