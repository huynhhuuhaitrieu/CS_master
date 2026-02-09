# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số

n = int(input("nhap so nguyen: "))
a = 1
while True:
    if n < 10:
        break
    if n // 10 != 0:
        a += 1
        n = n // 10
print("so vua nhap co so chu so la: ",a)