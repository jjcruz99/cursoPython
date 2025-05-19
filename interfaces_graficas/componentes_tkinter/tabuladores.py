
import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
from time import sleep

ventana = tk.Tk()
ventana.geometry('600x400+500+200')
ventana.title('Tabuladores')

def crear_componentes_tabulador1(tabulador1):
    #agregar elementos
    etiqueta1= ttk.Label(tabulador1,text='Nombre')
    etiqueta1.grid(column=0,row=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador1, width=30)
    entrada1.grid(row=0,column=1, pady=5,padx=5)
    def enviar():
        messagebox.showinfo('Mensaje', f'{entrada1.get()}')

    boton1 = ttk.Button(tabulador1,text='Enviar',command=enviar)
    boton1.grid(row=1,column=0,columnspan=2)

def crear_componentes_tabulador2(tabulador2):
    contenido ='hgsdjhdgfjhgjhfjhbvfjhgjkhghkjfdshgkjsdfhfgkjhfdsgkjhdfskjgh '
    scroll = scrolledtext.ScrolledText(tabulador2,width=50,height=10,wrap=tk.WORD)
    scroll.insert(tk.INSERT,contenido)
    scroll.grid(row=0,column=0)

def crear_componentes_tabulador3(tabulador3):
    #crear lista usando list comprehensions
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(tabulador3, width=15, values=datos)
    combobox.grid(row=0,column=0,padx=10,pady=10)
    #elemento por default
    combobox.current(0)
    #agregar botton para saber que selecciono
    def mostrar():
        messagebox.showinfo('Mostrar',f'{combobox.get()}')

    boton1 = ttk.Button(tabulador3,text='Mostrar',command=mostrar)
    boton1.grid(row=0,column=1)

def crear_componentes_tabulador4(tabulador4):
    #Imagenes
    imagen1 = tk.PhotoImage(file='python-logo.png')
    def mosmostrar_titulo():
        messagebox.showinfo('Titulo',f'Nombre imagen: {imagen1.cget("file")}')
    boton_imagen = ttk.Button(tabulador4,image=imagen1,command=mosmostrar_titulo) #se agrego imagen de fondo al boton
    boton_imagen.grid(row=0,column=0)

def crear_componentes_tabulador5(tabulador5):
    #barra de progreso
    barra_progreso = ttk.Progressbar(tabulador5,orient='horizontal',length=400)
    barra_progreso.grid(row=0,column=0,padx=5,pady=5,columnspan=4)

    #
    def ejecutar():
        barra_progreso['maximum'] = 100

        for valor in range(0,101,1):
            sleep(0.05)
            barra_progreso['value'] = valor
            barra_progreso.update()
        barra_progreso['value']=0

    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_segundos():
        delay_ms = 1000
        ventana.after(delay_ms, barra_progreso.stop())

    boton_inicio = ttk.Button(tabulador5,text='Ejecutar',command=ejecutar)
    boton_inicio.grid(row=1,column=0)
    boton_ciclo = ttk.Button(tabulador5,text='Ejecutar Ciclo',command=ejecutar_ciclo)
    boton_ciclo.grid(row=1,column=1)
    boton_detener = ttk.Button(tabulador5,text='Detener',command=detener)
    boton_detener.grid(row=1,column=2)
    boton_segundos = ttk.Button(tabulador5,text='Detener segundos',command=detener_segundos)
    boton_segundos.grid(row=1,column=3)
def crear_tabs():
    control_tabulador = ttk.Notebook(ventana)

    #agregar un frame para agregar dentro del tab
    tabulador1 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador1, text='Tabulador 1')
    control_tabulador.pack(fill='both')
    crear_componentes_tabulador1(tabulador1)

    #crear un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador,text='Contenido')
    control_tabulador.add(tabulador2,text='Tabulador 2')
    #crear componentes de tabulador2
    crear_componentes_tabulador2(tabulador2)

    #crear tabulador 3
    tabulador3= ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3,text='Tabulador 3')
    #crear componentes tab3
    crear_componentes_tabulador3(tabulador3)

    #crear tabulador 4
    tabulador4= ttk.LabelFrame(control_tabulador)
    control_tabulador.add(tabulador4,text='Tabulador 4')
    #crear componentes tab4
    crear_componentes_tabulador4(tabulador4)

    #crear tabulador 5
    tabulador5= ttk.LabelFrame(control_tabulador)
    control_tabulador.add(tabulador5,text='Tabulador 5')
    #crear componentes tab5
    crear_componentes_tabulador5(tabulador5)

crear_tabs()

ventana.mainloop()