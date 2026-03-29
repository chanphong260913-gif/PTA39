# oop: object-orinted proramming
# tạo lớp vật nuôi(giống, màu sắc, tuổi, cân nặng)

class Vatnuoi (object):
    def __init__(self, giong="", mauSac="", tuoi=0, canNang=0):
        # __ : pritave
        self.__giong = giong
        self.__mauSac = mauSac
        self.__tuoi = tuoi
        self.__canNang = canNang

def __str__(self) -> str:
    return f"Vatnuoi: {self.__giong}, {self.__mauSac}, {self.__tuoi}, {self.__canNang}"

# getter va setter (lấy và đặt giá trị thuộc tính)
# "get"/"set" + tenthuoc tinh
def getGiong (self):
    return self.__giong

def getMauSac (self):
    return self.__mauSac

def getTuoi (self):
    return self.__tuoi

def getCanNang (self):
    return self.__canNang

def setGiong (self, giongMoi):
    self.__mauSac = mauSacMoi

def setTuoi (self, tuoiMoi):
    self.__tuoi = tuoiMoi

def setCanNang (self, canNangMoi):
    self.__canNang = canNangMoi

# tạo đối tượng
meo1 = Vatnuoi("mèo","đen")
print(meo1)