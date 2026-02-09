# Nhập vào số nguyên dương n, tính tổng các chữ số của n

a = int(input("Nhap vao so nguyen duong n: "))
sum = 0

while a > 0 :

    b = a % 10
    sum += b
    a //= 10
print("Tong cac chu so: ",sum)
