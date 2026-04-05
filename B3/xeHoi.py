# lop con 2
from lopCha import Xe


class XeHoi(Xe):
    def __init__(self, hang="", mauSac="", giaTien=0):
        super().__init__(hang, mauSac, giaTien)
        
    #override
    def run(self):
        # goi lai thuoc tinh PRIVATE cua lop cha
        hang = self._Xe__hang
        return f"Xe {hang} dang duoc lai voi 4 banh"
    
# tao object
xeHoi1 = XeHoi("Hang 2", "Do + Den", 2000000)
print(xeHoi1) # ham duoc ke thua tu lop Xe
print(xeHoi1.khoiDong()) # ham duoc ke thua tu lop Xe
print(xeHoi1.run()) # ham duoc override tu lop Xe