import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):

    def __init__(self):
        super().__init__() #constructor de la clase padre
        #configurar ventana
        self.configurar_ventana() #Metodo de instancia
        #configurar grid
        self.configurar_grid()

        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('800x400')
        self.configure(background='#1d2d44')
        self.title('Ventana con POO')

    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)

    def mostrar_tabla(self):
        # definir estilos
        estilos = ttk.Style()
        estilos.theme_use('clam')
        estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])

        # definir las columnas
        columnas = ('Id', 'Nombre', 'Edad')
        # se hace referencia al objeto App que se crea por eso self = ventana en este caso
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')

        # cabeceros de la tabla
        self.tabla.heading('Id', text='Id')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('Edad', text='Edad', anchor=tk.E)  # alinea el texto de la cabecera a la DERECHA

        # formato a las columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)

        # cargar datos a la tabla
        datos = ((1, 'Vale', 25), (2, 'Ana', 32))
        # for para aumentar la cantidad de registros
        for contador in range(0, 5, 1):
            datos += datos

        for persona in datos:
            self.tabla.insert(parent='', index=tk.END,
                         values=persona)  # parent vacio no subregistros, tk.END se insertan en orden

        # sccrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # asociar el evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>',
                   self.mostrar_seleccionado)

            #publicar tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

    def mostrar_seleccionado(self,event):
        print('Ejecutando metodo')
        elemento_seleccionado = self.tabla.selection()[0]  # asiga el primer elemento seleccionado
        elemento = self.tabla.item(elemento_seleccionado)
        persona = elemento['values']  # obtener tupla de valores
        print(persona)
        showinfo(title='Selecionado', message=f'Datos: {persona}')

#pruebas locales
if __name__ == '__main__':
    app1 = App()
    app1.mainloop()

