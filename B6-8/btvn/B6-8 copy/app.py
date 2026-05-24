from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os

from pages.login import LoginPage  # trang dau tien truy cap

# lay duong dan den cac file con
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # ke thua cac code init cua lop cha
        # dat ten cho app
        self.setWindowTitle("Apdoption Pet App - Login")

        # load trang login tu LoginPage
        self.login_page = LoginPage(
            main_window=self, root_dir=BASE_DIR
        )  # truyen vao tham so man hinh hien tai
        
        self.setCentralWidget(self.login_page)  # dat login_page vao Main window       
        self.show()  # hien thi


# chi chay khi run bang app.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())