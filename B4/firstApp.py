from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from PyQt6 import uic

class Home(QMainWindow):
    def __init__(self):
        super().__init__() # kế thừa các thuộc tính từ lớp QMainWindow
        # load file giao diện
        uic.loadUi("b4/home.ui", self)
        # chạy app
        self.show()


app = QApplication(sys.argv)
home= Home()
sys.exit(app.exec())