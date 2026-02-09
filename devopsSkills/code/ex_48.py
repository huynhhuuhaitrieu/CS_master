# Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD:
# Nhập chuỗi: abd45ecf47wde3s1
# Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24

my_string = input("nhap chuoi ")
mylist=[]
for i in my_string:
    if i.isdigit():
        mylist.append(int(i))
tong = sum(mylist)
print("Tong cac so la: ",tong)
