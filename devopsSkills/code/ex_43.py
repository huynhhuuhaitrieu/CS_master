# Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)

s = input("nhap chuoi ")
danh_sach_tu = s.split()
soLuongTu = len(danh_sach_tu)
# print("danh sach tu", danh_sach_tu)
# print(type(s))
# print(type(danh_sach_tu[1]))
print("so luong tu ", soLuongTu)