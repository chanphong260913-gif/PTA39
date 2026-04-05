class HocSinh:
    def __init__(self, hoten, lop, truong, toan, van, anh):
        self.hoten = hoten
        self.lop = lop
        self.truong = truong
        self.toan = toan
        self.van = van
        self.anh = anh
    def diem_tb(self):
        return (self.toan + self.van + self.anh) / 3
    def hien_thi(self):
        print(self.hoten, "-", self.lop, "-", self.truong, "- TB:", self.diem_tb())

ds = []
ds.append(HocSinh("An", "10A1", "THPT A", 2, 7, 9))
ds.append(HocSinh("Bình", "10A2", "THPT B", 10, 6, 8))
ds.append(HocSinh("Cường", "10A3", "THPT C", 1, 3, 8))

max_tb = ds[0].diem_tb()
for hs in ds:
    if hs.diem_tb() > max_tb:
        max_tb = hs.diem_tb()

print("Học sinh có điểm TB cao nhất:")
for hs in ds:
    if hs.diem_tb() == max_tb:
        hs.hien_thi()