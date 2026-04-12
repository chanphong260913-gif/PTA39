# - Tên ngân hàng  # khong thay doi
# - Tên chủ tài khoản  
# - Số tài khoản  # khong thay doi
# - Số tiền trong tài khoản  # in - out
class BankAccount():
    def __init__(self, tenTaiKhoan, tenNganHang, soTaiKhoan, soTien):
        self.__tenTaiKhoan = tenTaiKhoan
        self.__tenNganHang = tenNganHang
        self.__soTaiKhoan = soTaiKhoan
        self.__soTien = soTien
        
    # Getter và Setter cho các thuộc tính
    def getTenTaiKhoan(self):
        return self.__tenTaiKhoan
    def setTenTaiKhoan(self, tenTaiKhoan):
        self.__tenTaiKhoan = tenTaiKhoan
    def getTenNganHang(self):
        return self.__tenNganHang
    def getSoTaiKhoan(self):
        return self.__soTaiKhoan
    def getSoTien(self):
        return self.__soTien
    
    # in thong tin tai khoan
    def __str__(self) -> str:
        return f'Tên tài khoản: {self.__tenTaiKhoan}\nTên ngân hàng: {self.__tenNganHang} - Số tài khoản: {self.__soTaiKhoan}\nSố tiền: {self.__soTien}'
    
    # nap tien vao tai khoan
    def napTien(self, soTienNap):
        if soTienNap > 0:
            self.__soTien += soTienNap
            print(f'Đã nạp {soTienNap} vào tài khoản. Số tiền hiện tại: {self.__soTien}')
        else:
            print('So tien nap phai lon hon 0.')    
        
    # rut tien tu tai khoan
    def rutTien(self, soTienRut):
        if soTienRut > self.__soTien:
            print('Số tiền rút vượt quá số tiền hiện có trong tài khoản.')
        elif soTienRut <= 0:
            print('Số tiền rút phải lớn hơn 0.')
        else:
            self.__soTien -= soTienRut
            print(f'Đã rút {soTienRut} từ tài khoản. Số tiền hiện tại: {self.__soTien}')


taikhoan1 = BankAccount("Phạm Chấn Phong", "Vietcombank", "3667", 36000000)
print(taikhoan1)
taikhoan1.napTien(360000)
taikhoan1.napTien(1)
taikhoan1.rutTien(36000000000000000000000000000)
taikhoan1.rutTien(1)