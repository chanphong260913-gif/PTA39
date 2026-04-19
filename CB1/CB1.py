class HocSinh:
    def __init__(self, hoTen, diaChi, chieuCao, canNang, hocLuc):
        self.hoTen = hoTen
        self.diaChi = diaChi
        self.chieuCao = chieuCao
        self.canNang = canNang
        self.hocLuc = hocLuc

    def thongTin(self):
        print(f"Họ tên: {self.hoTen}. Địa chỉ: {self.diaChi}. Chiều cao: {self.chieuCao} cm. Cân Nặng: {self.canNang} Kg. Học lực: {self.hocLuc}.")

    def diaChiMoi(self, diaChiMoi):
        self.diaChi = diaChiMoi
        print(f"Đã cập nhật địa chỉ của học sinh {self.hoTen}!")

    def sucKhoe(self, chieuCaoMoi, canNangMoi):
        self.chieuCao = chieuCaoMoi
        self.canNang = canNangMoi
        print(f"Đã cập nhật chiều cao, cân nặng của học sinh {self.hoTen}!")

hs1 = HocSinh("Nguyễn Văn An", "Bến Tre", 134, 36, "Giỏi")
hs2 = HocSinh("Phạm Hoàng Minh", "Hà Nội", 170, 100, "Yếu")
hs3 = HocSinh("Võ Tuấn Đạt", "Nghệ An", 169, 67, "Khá")
hs1.thongTin()
hs2.thongTin()
hs3.thongTin()
hs1.diaChiMoi("Hải Phòng")
hs1.sucKhoe(190, 85)
hs2.sucKhoe(175,40)
hs1.thongTin()
hs2.thongTin()
hs3.thongTin()