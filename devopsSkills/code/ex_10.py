while True:
    try:
        salary = int(input("Your salary "))

        salary = int(salary*0.9)


        print("salary: ", salary)
    
    except ValueError:
        print("Please enter an integer")
