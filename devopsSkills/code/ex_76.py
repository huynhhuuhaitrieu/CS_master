# .Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
def so_lon_nhat(deflist):
    a = deflist[0]
    b=0
    for i in range(1,len(deflist)):
        if a < deflist[i]:
            a = deflist[i]
            b=i
    print("vi tri so lon nhat trong day la: ",b+1)


mylist = list(map(int,input("nhap day so nguyen: ").split()))
so_lon_nhat(mylist)
