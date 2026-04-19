# main.py
import sys
from PyQt5 import QtWidgets, uic

class DangNhap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dangnhap.ui", self)   # nạp file .ui

        # kết nối nút bấm
        self.btnDangNhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()

        if username == "admin" and password == "123":
            QtWidgets.QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")
        else:
            QtWidgets.QMessageBox.warning(self, "Thông báo", "Sai tài khoản hoặc mật khẩu!")

app = QtWidgets.QApplication(sys.argv)
window = DangNhap()
window.show()
sys.exit(app.exec_())