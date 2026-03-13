# Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó

def bang_cuu_chuong(x):
    print(f"Bang cuu chuong {x}:")
    for i in range(1,11):
        print(f"{x} x {i} = {x*i}")

a,b = map(int,input("nhap 2 so a, b: ").split())
x = max(a,b)

bang_cuu_chuong(x)