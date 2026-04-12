#	Gửi tặng cô giáo đáng yêu của em:
#	Tài Khoản: tung tung tung shaur like eat chip chip and donut
#	Mật khẩu: I am tung tung tung tung tung sahur not like eat chip chip, donut and if you enter this line I think you so tung tung tung
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#           TÊN VÀ MẬT KHẨU CÓ HƠI DÀI NÊN CÔ THÔNG CẢM!

class BankAccount:
    def __init__(self):
        self.nguoiDung = "tung tung tung shaur like eat chip chip donut"
        self.mK = "I am tung tung tung tung tung sahur not like eat chip chip, donut and if you enter this line I think you so tung tung tung sahur"
        self.tien = 2000000

    def dang_nhap(self):
        print("== Ngân hàng Vietcombank ==")
        nguoiDung_nhap = input("Nhập tên tài khoản: ")
        mK_nhap = input("Nhập mật khẩu: ")
        
        if nguoiDung_nhap == self.nguoiDung and mK_nhap == self.mK:
            print("Đăng nhập thành công!")
            self.menu()
        else:
            print("Mật khẩu sai, vui lòng nhập lại")
            self.dang_nhap()

    def menu(self):
        print("== Ngân hàng Vietcombank ==")
        print("1. Số dư tài khoản")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")
        chon = input("Chọn: ")
        
        if chon == "1": 
            print("Số dư của bạn là:", self.tien)
            self.menu()
        elif chon == "2": 
            tien_nap = input("Nhập số tiền nạp: ")
            self.tien = self.tien + int(tien_nap)
            print("Nạp thành công, tài khoản còn:", self.tien)
            self.menu()
        elif chon == "3":
            so_tien_rut = input("Nhập số tiền rút: ")
            so_tien_rut = int(so_tien_rut)
            if so_tien_rut <= self.tien:
                self.tien = self.tien - so_tien_rut
                print("Rút thành công, còn:", self.tien)
            else:
                print("Không đủ tiền!")
            self.menu()
        elif chon == "4": 
            print("Tạm biệt")
            exit()

# Chạy chương trình
bank = BankAccount()
bank.dang_nhap()