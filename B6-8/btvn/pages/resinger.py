from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class ResingerPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir

        # load ui
        ui_path = self.root_dir + "/GUI/resinger.ui"
        uic.loadUi(ui_path, self)

        # nút quay lại login
        self.nav_register.clicked.connect(
            self.goto_login
        )

    # ---------------- QUAY LẠI LOGIN ----------------
    def goto_login(self):
        from pages.login import LoginPage

        login_page = LoginPage(
            main_window=self.main_window,
            root_dir=self.root_dir
        )

        self.main_window.setCentralWidget(login_page)