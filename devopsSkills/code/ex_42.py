# Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A


a = int(input("nhap so a: "))
my_list=[1,1]
while a >= my_list[len(my_list)-1]:
    fib = my_list[len(my_list)-1] + my_list[len(my_list)-2]
    my_list.append(fib)
print("so lon nhat trong day fib la ",my_list[len(my_list)-2])
