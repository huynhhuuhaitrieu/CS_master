# Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)

s = input("nhap chuoi ")
a=0
for i in s:
    a += 1

print("so ky tu trong chuoi ", a)