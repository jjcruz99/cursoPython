import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

##crear objeto encargado de procesar todos los objetos
app = QApplication()

# Crear un objeto ventana
ventana = QWidget()

#mostrar la ventana
ventana.show()

#ajustar ventana
ventana.setWindowTitle("Hola Mundo -  Mi primera ventana")
ventana.resize(600,400)

# cualquier componente puede ser una ventana en pyside
# boton = QPushButton("Boton")
# boton.show()

 #ejecutar aplicacion
sys.exit(app.exec())




