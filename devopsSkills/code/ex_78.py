# .Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list
def chuoi_ngan_nhat(x):
    a = x[0]
    for i in range (1,len(x)):
        if len(a)> len(x[i]):
            a = x[i]
    print("chuoi co do dai ngan nhat la: ",a)

mylist = list(input("nhap list cac chuoi cua ban: ").split())

chuoi_ngan_nhat(mylist)