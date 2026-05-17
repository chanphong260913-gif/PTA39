import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        path = os.path.join(os.path.dirname(__file__), "1.ui")
        uic.loadUi(path, self)

        self.show()

app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())