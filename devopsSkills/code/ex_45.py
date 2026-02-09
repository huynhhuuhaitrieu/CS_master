# Nhập vào một chuỗi, hãy xóa từ cuối cùng trong chuỗi


chuoi = input("nhap chuoi ")
danhSachTu = chuoi.split()
danhSachTu.pop()
print("Tu cuoi cung la: ",danhSachTu[-1])