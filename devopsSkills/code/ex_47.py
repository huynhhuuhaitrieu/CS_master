# Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số

my_string = input("nhap chuoi ")
soChuHoa = 0
soChuThuong = 0
soKyTuSo = 0
for i in my_string:
    if i.islower():
        soChuThuong += 1
    if i.isupper():
        soChuHoa += 1
    if i.isdigit():
        soKyTuSo += 1
         


print("so chu hoa, thuong,so:",soChuHoa,soChuThuong,soKyTuSo)