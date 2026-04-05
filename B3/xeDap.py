# lớp con 1
from lopCha import Xe


class XeDap(Xe):
    def __init__(self, hang="", mauSac="", giaTien=0):
        super().__init__(hang, mauSac, giaTien)
    
    # override
    def run(self):
        # gọi lại thuộc tính private của lớp cha
        hang = self._Xe__hang
        return f"Xe {hang} đang được đạp"
    
# tao object
xeDap1 = XeDap("Hang 1", "Xanh la + Tim", 1000)
print(xeDap1) # ham duoc ke thua tu lop Xe
print(xeDap1.khoiDong()) # ham duoc ke thua tu lop Xe
print(xeDap1.run()) # ham duoc override tu lop Xe