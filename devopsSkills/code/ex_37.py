import math
result_max = -math.inf
result_min = math.inf

while True:
    n = int(input("nhap so nguyen: "))
    if n == -1:
        break
    if n > result_max:
        result_max = n
    if n < result_min:
        result_min =n

    # print(my_list)
    print("max",result_max)
    print("min",result_min)