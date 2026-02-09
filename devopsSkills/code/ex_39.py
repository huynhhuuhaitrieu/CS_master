# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số le

a = int(input("nhap vao so nguyen duong: "))
soSoChan = 0
soSoLe = 0
my_list= []
while a > 0:
    b = a % 10        
    if b % 2 == 0:
        soSoChan +=1
    else:
        soSoLe +=1
    a //= 10
print("So so chan",soSoChan)
print("So so le",soSoLe)      





