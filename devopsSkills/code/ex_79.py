# Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L


def average(listSoNguyen,x):

    newlist = mylist[:x]
    output = sum(newlist)/len(newlist)
    print("gia tri trung binh la: ", output)

mylist = list(map(int,input("nhao day so nguyen: ").split()))
a = int(input("nhap so a: "))
average(mylist,a)

