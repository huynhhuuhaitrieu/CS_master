# 54.Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b

my_list = list(map(int, input("nhap day so nguyen: ").split()))
print("my_list: ", my_list)
a,b = map(int,input("nhap 2 so a va b: ").split())
print("a va b: ",a,b)

new_list = my_list[a:b]
print(new_list)
print("max",max(new_list))
