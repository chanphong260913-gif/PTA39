from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os


class LoginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__() # ker thua cac code init cua lop cha
        self.main_window = main_window # luu tham so
        self.root_dir = root_dir

        # load file ui
        ui_path = self.root_dir + "/GUI/login.ui"
        uic.loadUi(ui_path,self)


        # bat su kien ut bam
        # 1. nut login
        self.login.clicked.connect(self.handle_login) # click vao nut login -> gioi ham handle login
        # 2. nut chuyen register
        self.nav_register.clicked.connect(self.goto_register)
    # -------------------- xu ly su kien --------------------
    def handle_login(self):
        # lay du lieu tu input form
        email_input = self.email.text().strip() # lay du lieu tu email input, xo khang trang 2 dau
        password_input = self.password.text()

        # validate du lieu
        if (self.__validate_input(email_input, password_input) is not None):
            # co loi -> bao loi
            self.show_message(self.__validate_input(email_input,password_input))
        
    def goto_register(self):
        from pages.resinger import RegisterPage
        register_page = RegisterPage(main_window=self.main_window,
                         root_dir=self.root_dir)   
             
    # -------------------- ham ho tro --------------------
    def goto_home(self):
        from pages.home import HomePage
        home_page = HomePage(main_window=self.main_window,
                         root_dir=self.root_dir)

    def __validate_input(self, email, password):
        # kiem tra email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(regex, email) is None:
            return "Email khong hop le"
        
        #kiem tra password
        if email != account['email'] or password != accout['password']:
            return "Email hoac password khong chinh xac"
        
        return None # khong co loi
    
    def show_message(self):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Đây là nội dung thông báo của bạn!")
        msg.setIcon(QMessageBox.Icon.Information) # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok) # Nút bấm OK
        
        # Hiển thị hộp thoại
        msg.exec()