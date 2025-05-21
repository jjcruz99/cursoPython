import tkinter as tk
from sys import exec_prefix
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

        #  reglon 1 de botones
        boton_borrar = tk.Button(botones_frame,text='C',
                                 bd=0,bg='#eee',cursor='hand2',
                                 width='32',height=3,command=self._borrar)
        boton_borrar.grid(row=0,column=0,columnspan=3,pady=1,padx=1)

        #crear el boton he insertarlo directramente con grid
        tk.Button(botones_frame, text='/',
                  bd=0, bg='#eee', cursor='hand2',
                  width='10', height=3, command=lambda: self._evento_click('/')).grid(row=0, column=3, pady=1, padx=1)


        #  reglon 2 de botones
        boton_siete = tk.Button(botones_frame, text='7',bd=0, bg='#FFF', cursor='hand2',
                                   width='10', height=3, command=lambda: self._evento_click('7'))
        boton_siete.grid(row=1,column=0,padx=1,pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('8'))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('9'))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicacion = tk.Button(botones_frame, text='*', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('*'))
        boton_multiplicacion.grid(row=1, column=3, padx=1, pady=1)

        #  reglon 3 de botones
        boton_cuatro = tk.Button(botones_frame, text='4',bd=0, bg='#FFF', cursor='hand2',
                                   width='10', height=3, command=lambda: self._evento_click('4'))
        boton_cuatro.grid(row=2,column=0,padx=1,pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('5'))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('6'))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_resta = tk.Button(botones_frame, text='-', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)


        #  reglon 4 de botones
        boton_uno = tk.Button(botones_frame, text='1',bd=0, bg='#FFF', cursor='hand2',
                                   width='10', height=3, command=lambda: self._evento_click('1'))
        boton_uno.grid(row=3,column=0,padx=1,pady=1)

        boton_dos = tk.Button(botones_frame, text='2', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('2'))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('3'))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_suma = tk.Button(botones_frame, text='+', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        #  reglon 5 de botones
        boton_cero = tk.Button(botones_frame, text='0',bd=0, bg='#FFF', cursor='hand2',
                                   width='10', height=3, command=lambda: self._evento_click('0'))
        boton_cero.grid(row=4,column=0,padx=1,pady=1)

        boton_punto = tk.Button(botones_frame, text='.', bd=0, bg='#FFF', cursor='hand2',
                                width='10', height=3, command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=1, padx=1, pady=1)

        boton_igual = tk.Button(botones_frame, text='=', bd=0, bg='#FFF', cursor='hand2',
                                width='21', height=3, command=self._evento_evaluar)
        boton_igual.grid(row=4, column=2, padx=1, pady=1,columnspan=2)


    #metodos operaciones
    def _borrar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self,elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        try :
            if self.expresion:
                # eval() evalua una la expresion str como si fuera una operacion matematica al contener operadores
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error',f'Error : {e}')
            self.expresion=''
        finally:
            self.expresion = ''



if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()