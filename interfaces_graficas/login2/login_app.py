import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title("Login")
ventana.configure(background='#1d2d44')

#grid de la ventana
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

#agregar frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=3)

#titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial',20))
etiqueta.grid(row=0,column=0,columnspan=2)

#usuario
etiqueta_usuario = ttk.Label(frame, text='Usuario', font=('Arial',16))
etiqueta_usuario.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)

#clave
etiqueta_clave = ttk.Label(frame, text='Password', font=('Arial',16))
etiqueta_clave.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)

clave_caja_texto = ttk.Entry(frame,show='*')
clave_caja_texto.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)

def validar(event):
    usuario = usuario_caja_texto.get()
    password = clave_caja_texto.get()
    if usuario =='root' and password == 'admin':
        messagebox.showinfo(title='Login',message='Datos correctos')
    else:
        messagebox.showerror(title='Login', message='Datos incorrectos')

#boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

#eventos del boton
login_boton.bind('<Return>',validar) #llama al evento validar al presionar enter
login_boton.bind('<Button-1>',validar) #llama al evento validar al presionar click izq


#Estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana,background='#1d2d44',foreground='white',fieldbackground='black')
estilos.configure('TButton',background='#005f73')
estilos.map('TButton',background=[('active','#0A9396')])


# publicar
frame.grid(column=0,row=0)
ventana.mainloop()