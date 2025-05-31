import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror

#crear ventana principal
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Mane de tabla')

#configurar el grid
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=0)

#definir estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('Treeview',background='black',foreground='white',fieldbackground='black',rowheight=30)
estilos.map('Treeview',background=[('selected' , '#3a86ff')])

#definir las columnas
columnas = ('Id','Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas,show='headings')


#cabeceros de la tabla
tabla.heading('Id',text='Id')
tabla.heading('Nombre',text='Nombre')
tabla.heading('Edad',text='Edad',anchor=tk.E) #alinea el texto de la cabecera a la DERECHA

# formato a las columnas
tabla.column('Id',width=80)
tabla.column('Nombre',width=120)
tabla.column('Edad',width=120)

#cargar datos a la tabla
datos=((1,'Vale',25),(2,'Ana',32))
# for para aumentar la cantidad de registros
for contador in range(0,5,1):
    datos += datos

for persona in datos:
    tabla.insert(parent='',index=tk.END, values=persona)#parent vacio no subregistros, tk.END se insertan en orden

#sccrollbar
scrollbar = ttk.Scrollbar(ventana,orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0,column=1,sticky=tk.NS)


def mostrar_seleccionado(event):
    print('Ejecutando metodo')
    elemento_seleccionado = tabla.selection()[0] #asiga el primer elemento seleccionado
    elemento = tabla.item(elemento_seleccionado)
    persona = elemento['values'] # obtener tupla de valores
    print(persona)
    showinfo(title='Selecionado',message=f'Datos: {persona}')

#asociar el evento select de la tabla
tabla.bind('<<TreeviewSelect>>',mostrar_seleccionado) #llama al metodo mostrar_seleccionado() al seleccionar una registro de la tabla


tabla.grid(row=0,column=0,sticky=tk.NSEW)
ventana.mainloop()