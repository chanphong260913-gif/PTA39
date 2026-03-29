a = input("Nhập giờ, phút, giây (hh, mm, ss): ")
b = a.split(":")

h = int(b[0])
m = int(b[1])
s = int(b[2])

if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("Hợp lệ!")
else:
    print("Không hợp lệ!")