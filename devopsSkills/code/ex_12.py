while True:
    try:
        str_input = input("Enter values for a, b, c (separated by space): ")
        a, b, c = map(float, str_input.split())

        d = (a+b)*c

        if 100 <= d <= 200:
            print("True")
        else:
            print("False")
    
    except ValueError:
        print("Please enter an integer")
