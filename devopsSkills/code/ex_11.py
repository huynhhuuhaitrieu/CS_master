while True:
    try:
        str_input = input("Enter values for a, b, c (separated by space): ")
        a, b, c = map(float, str_input.split())

        sum = float(a+b+c)


        print("sum: ", sum)
    
    except ValueError:
        print("Please enter an integer")
