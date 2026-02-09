h = int(input("Nhập chiều cao h: "))

print(f"\nKết quả với h = {h}:")

for i in range(1, h + 1):
    # Tính số khoảng trắng bên trái để đẩy tam giác ra giữa
    khoang_trang_trai = " " * (h - i)
    
    if i == 1:
        # Dòng đầu tiên: Chỉ 1 ngôi sao
        print(khoang_trang_trai + "*")
        
    elif i == h:
        # Dòng cuối cùng: In hết sao (số lượng = 2*h - 1)
        print("*" * (2 * h - 1))
        
    else:
        # Các dòng ở giữa: Sao + Khoảng trắng rỗng + Sao
        # Công thức tính khoảng trắng ở giữa: 2*i - 3
        khoang_trang_giua = " " * (2 * i - 3)
        print(khoang_trang_trai + "*" + khoang_trang_giua + "*")