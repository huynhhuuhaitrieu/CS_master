while True:
    try:
        str_input = input("Enter values for a, b (separated by space): ")
        a, b = map(int, str_input.split())
        list_uc = []
        if a <= b:
            c = a
        else:
            c = b
      
        
        for i in range(1,c+1):
            if a % i == 0 and b % i == 0:
                list_uc.append(i)

        print (list_uc)


    
    except ValueError:
        print("Please enter an integer")
