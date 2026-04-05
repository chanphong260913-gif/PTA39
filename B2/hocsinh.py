from btvn2s import QuanLyDiemHocSinh

hs1 = QuanLyDiemHocSinh("Meo", "12A1", "THPT Nguyen Hue", 8, 7, 9)
hs2 = QuanLyDiemHocSinh("Mèo", "12F4", "THPT Nguyen Hue", 10, 10, 9.5)
hs3 = QuanLyDiemHocSinh("Méo", "12A1", "THPT Nguyen Hue", 10, 9.5, 10)
hs4 = QuanLyDiemHocSinh("Mẽo", "12B3", "THPT Nguyen Hue", 7, 10, 10)
hs5 = QuanLyDiemHocSinh("Mẻo", "12A1", "THPT Nguyen Hue", 6, 4, 6)
hs6 = QuanLyDiemHocSinh("Mẹo", "12A3", "THPT Nguyen Hue", 10, 5, 1)

# hiển thị học sinh đúng nhất (nếu như có nhiều học sinh = diem max -> hiển thị hết)
# tìm điểm trung bình cao nhất
diemTBMax = max(
    hs1.tinhDiemTrungBinh(),
    hs2.tinhDiemTrungBinh(),
    hs3.tinhDiemTrungBinh(),
    hs4.tinhDiemTrungBinh(),
    hs5.tinhDiemTrungBinh(),
    hs6.tinhDiemTrungBinh(),
)

# hiển thị thông tin hs max tb
for hs in [hs1, hs2, hs3, hs4, hs5, hs6]: # duyệt qua danh sách học sinh
    if (hs.tinhDiemTrungBinh() == diemTBMax): # nếu điểm trung bình của học sinh hiện tại = max
        print(hs)