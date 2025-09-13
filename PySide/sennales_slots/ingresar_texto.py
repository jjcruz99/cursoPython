from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget
import  sys


class VentanaPrincipal(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Signals y slots")
        self.setFixedSize(400,200)
        #Definir los componentes
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #Conectar de entrada de texto con la etiqueta
        #Los eventos no () por que solo se estan asociando
        #la señal es textChanged y el evento es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)

        #Publicar los componentes usando un layout
        #caja vertical
        disposcision  = QVBoxLayout()
        disposcision.addWidget(self.entrada_texto)
        disposcision.addWidget(self.etiqueta)

        #crear contenedor para publicar layout
        contenedor = QWidget()
        contenedor.setLayout(disposcision)
        #Publicar contenedor
        self.setCentralWidget(contenedor)





if __name__ == "__main__":

    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())