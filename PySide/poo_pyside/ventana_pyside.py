import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


## Hereda de QMainWindow
class VentanaPySide(QMainWindow):

    def __init__(self):
        #llamar al metodo init de la clase padre
        super().__init__()
        #Configurar ventana
        self.setWindowTitle("Ventana POO")
        #self.resize(800,500)
        #Configurar el tamaño fijo de la ventana
        self.setFixedSize(QSize(600,400))
        #crear de los componentes con un metodo de clase
        self._agregar_componentes()

    #metodo de la clase
    def _agregar_componentes(self):

        #Agregar menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
         #agregar opciones al menu principal
        accion_nuevo = QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
         #Agregar un texto a la barra de estado cuando abra el menu
        accion_nuevo.setStatusTip('Nuevo archivo')

         #Agregar un mensaje en la barra de estado "parte inferior"
        self.statusBar().showMessage('Infromacion barra de estado')

         #Crear y Agregar un boton
        boton = QPushButton("NuevoBoton")
        self.setCentralWidget(boton)




if __name__ == "__main__":

    ## se pasa una lista []
    app = QApplication([])

    #crear ventana
    ventana = VentanaPySide()
    ventana.show()
    sys.exit(app.exec())
