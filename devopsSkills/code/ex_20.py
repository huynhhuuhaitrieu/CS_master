while True:
    try:
        month = int(input("Month "))
        if month < 1 or month > 12:
            raise ValueError




        year = int(input("Year "))

        listOfMonth_31 =[1,3,5,7,8,10,12]
        listOfMonth_30 =[4,6,9,11]

        if month in listOfMonth_31:
            print("31 days")

        elif month in listOfMonth_30:
            print("30 days")

        elif month == 2 :
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("29 days")
                
            else:
                print("28 days")

    
    except ValueError:
        print("Invalid input! Please enter an integer (Month 1-12).")
