# Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không

a = int(input("nhap vao 1 so nguyen duong: "))
k=0
if a == 1:
    print("n co dang 2^0")  
else:
    while a % 2 == 0:
        k += 1
        a //= 2
    if (k > 0) and (a ==1):    
        print("n co dang 2^",k)
    else:
        print("n ko co dang 2^k")
