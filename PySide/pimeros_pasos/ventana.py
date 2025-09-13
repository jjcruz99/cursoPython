import sys
from PySide6.QtWidgets import QApplication,QMainWindow

app = QApplication()

ventana = QMainWindow()
ventana.setWindowTitle("Ventana principal")
ventana.resize(800,500)
ventana.show()

sys.exit(app.exec())
