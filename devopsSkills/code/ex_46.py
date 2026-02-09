# Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
# VD:
# Nhập: 3, 12, 15
# Tổng: 30
str_input = input("Enter values for a, b, c (separated by ,): ")
danhSachSo = list(map(int, str_input.split(",")))

tong = sum(danhSachSo)
print("tong la: ",tong)