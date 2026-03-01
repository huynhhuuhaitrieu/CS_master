# 56.Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list,
# nếu không có giá trị dương, ta in ra -1

mylist = list(map(int,input("Nhap day so nguyen: ").split()))

result = -1

for i in range(len(mylist)):
    if mylist[i] > 0:
        result = mylist[i]
        break

print("Ket qua la: ",result)
