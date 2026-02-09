import math


while True:
    try:
        a = int(input("Nhap so: "))
        #list_uc = []
        kq = math.sqrt(a)
        
        if a <2:
           print (a, " không là số nguyên tố")
        else: 
            for i in range(2,kq+1):

                if kq % i ==0:
                    print (a, "là số nguyên tố")
                else:
                    print (a, " không là số nguyên tố")


    
    except ValueError:
        print("Please enter an integer")
