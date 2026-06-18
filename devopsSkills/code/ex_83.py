# Viết hàm đưa vào 1 dictionary có các phần tử có key là chuỗi, tìm và trả về giá trị của key có độ dài lớn nhất


n = int(input("So phan tu muon nhap: "))
mydict = {}
for i in range(0,n):
    key = input("Nhap gia tri cua key {i}")
    value = len(key)
    mydict[key]=value
maxkey = max(mydict,key=mydict.get)
output = mydict[maxkey]
print(output)
