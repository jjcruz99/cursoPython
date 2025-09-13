# signals = eventos
# slots = funciones procesan los eventos
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

class VentanaPrincipal(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Signals y slots")

        #crear y agregar un boton
        boton = QPushButton('Click')
        #conectar el evento checado(por default es Flase)
        boton.setCheckable(True)
        #conectar otro slot al evento de  checar
        boton.clicked.connect(self.evento_checar)
        #Conectar la signal click con el slot (evento_click)
        boton.clicked.connect(self.evento_click)
        self.setCentralWidget(boton)

    def evento_click(self):
        print("Has echo click")
        print(f"Boton checado desde evento_click {self.boton_checado}")

    def evento_checar(self,checar):
        self.boton_checado = checar
        print(f"Checado {self.boton_checado}")

if __name__ == "__main__":

    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
