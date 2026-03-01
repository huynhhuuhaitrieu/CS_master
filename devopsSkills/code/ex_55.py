# 55.Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong
# mảng có bằng nhau hay không, nếu có thì in True, không có thì in False

mylist = list(map(int,input("nhap cac so nguyen: ").split()))
result = "True"
for i in range (len(mylist)-1):
    if mylist[i] != mylist[i+1]:
        result = "False"
print("Ket qua la: ",result)
