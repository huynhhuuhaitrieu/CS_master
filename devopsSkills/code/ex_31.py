while True:
    try:
        str_input = input("Enter values for a, b (separated by space): ")
        a, b = map(int, str_input.split())
        arr = []
        if a <= b:
            c = a
        else:
            c = b
      
        
        for i in range(1,c+1):
            if a % i == 0 and b % i == 0:
                arr.append(i)

        print (arr)


    
    except ValueError:
        print("Please enter an integer")
