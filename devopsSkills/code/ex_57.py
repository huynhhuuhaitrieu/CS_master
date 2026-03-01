# 57.Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0


mylist = list(map(int,input("nhap list so nguyen: ").split()))
negative = [x for x in mylist if x < 0]
print("ket qua la: ", max(negative) if negative else 0)