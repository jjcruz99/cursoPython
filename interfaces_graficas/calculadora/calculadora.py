import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('400x500')
        self.title('Calculadora')
        self.resizable(0,0)
        #atributos
        self.expresion = ''
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self._creacion_componentes()

    def _creacion_componentes(self):
        #crear frame para la caja de texto
        entrada_frame = tk.Frame(self,width=450,height=50)
        entrada_frame.pack(side=tk.TOP)
        entrada = tk.Entry(entrada_frame,font=('arial',14,'bold'),textvariable=self.entrada_texto,width=25,justify=tk.RIGHT)
        entrada.grid(row=0,column=0,ipady=5,pady=10)

        # crear frame para los botones
        botones_frame = tk.Frame(self,width=440,height=500,background='grey')
        botones_frame.pack()

        boton_borrar = tk.Button(botones_frame,text='C',
                                 bd=0,bg='#eee',cursor='hand2',
                                 width='32',height=3,command=self._borrar)
        boton_borrar.grid(row=0,column=0,columnspan=3,pady=1,padx=1)

        boton_division=tk.Button(botones_frame, text='/',
                  bd=0, bg='#eee', cursor='hand2',
                  width='10', height=3, command=lambda: self._evento_click('/')).grid(row=0, column=3, pady=1, padx=1)

    #metodos operaciones
    def _borrar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self,elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()