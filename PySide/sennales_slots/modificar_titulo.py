from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
import  sys
class VentanaPrincipal(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Signals y slots")
        #crear y agregar un boton
        self.boton = QPushButton('Click')
        #Asociar la señal de click al evento clic
        self.boton.clicked.connect(self.evento_click)
        #Conectar la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        self.setCentralWidget(self.boton)

    def evento_click(self):
        #cambiar textod el boton
        self.boton.setText("Nuevp texto")
        self.boton.setEnabled(False)
        self.setWindowTitle("Cambio de titulo de la APP desde evento_click")
        print("Boton desabilitado")

    def cambio_titulo_aplicacion(self,nuevo_titulo):
        print(f'Nuevo titulo: {nuevo_titulo}')

if __name__ == "__main__":

    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())