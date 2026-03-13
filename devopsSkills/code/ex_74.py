# Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không

import math

def kiem_tra_so_nguyen_to(x):
    # Bước 1: Loại bỏ các số bé hơn 2
    if x < 2:
        return False
    
    # Bước 2: Kiểm tra từ 2 đến căn bậc hai của x (tối ưu nhất)
    # Hoặc đơn giản là range(2, int(x**0.5) + 1)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # Nếu thấy một ước, thoát và trả về False ngay
            
    # Bước 3: Nếu chạy hết vòng lặp mà không chia hết cho số nào
    return True

a = int(input("Nhap so a: "))
if kiem_tra_so_nguyen_to(a):
    print(f"{a} là số nguyên tố")
else:
    print(f"{a} không phải là số nguyên tố")