from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import re

# tài khoản test
account = {
    "email": "admin@gmail.com",
    "password": "123456"
}


class LoginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir

        # load ui
        ui_path = self.root_dir + "/GUI/login.ui"
        uic.loadUi(ui_path, self)

        # sự kiện
        self.login.clicked.connect(self.handle_login)
        self.nav_register.clicked.connect(self.goto_register)

    # ---------------- LOGIN ----------------
    def handle_login(self):
        email_input = self.email.text().strip()
        password_input = self.password.text()

        error = self.__validate_input(
            email_input,
            password_input
        )

        if error is not None:
            self.show_message(error)
            return

        self.show_message("Đăng nhập thành công!")

    # ---------------- CHUYỂN REGISTER ----------------
    def goto_register(self):
        from pages.resinger import ResingerPage

        register_page = ResingerPage(
            main_window=self.main_window,
            root_dir=self.root_dir
        )

        self.main_window.setCentralWidget(register_page)

    # ---------------- VALIDATE ----------------
    def __validate_input(self, email, password):

        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # kiểm tra email
        if re.fullmatch(regex, email) is None:
            return "Email không hợp lệ"

        # kiểm tra tài khoản
        if (
            email != account["email"]
            or
            password != account["password"]
        ):
            return "Email hoặc password không chính xác"

        return None

    # ---------------- THÔNG BÁO ----------------
    def show_message(self, text):
        msg = QMessageBox()

        msg.setWindowTitle("Thông báo")
        msg.setText(text)

        msg.setIcon(QMessageBox.Icon.Information)

        msg.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )

        msg.exec()