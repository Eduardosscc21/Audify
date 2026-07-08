# ventana_cargar.py
from PySide6.QtWidgets import QApplication
from audify import MainWindow
import sys

# Iniciar aplicación
app = QApplication(sys.argv)

# Crear ventana
window = MainWindow()
window.show()

# Ejecutar
sys.exit(app.exec())