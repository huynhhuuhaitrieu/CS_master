while True:
    try:
        listOfDay =[0,31,28,31,30,31,30,31,31,30,31,30,31]
        month = int(input("Month "))
        if month < 1 or month > 12:
            raise ValueError

        day = int(input("Day "))
        if day < 1 or day > 31:
            raise ValueError

        if day < 1 or day > listOfDay[month]:
            raise ValueError(f"Tháng {month} chỉ có tối đa {listOfDay[month]} ngày!")


        for i in range (month):
            day = listOfDay[i] + day
        
        print(day)

    
    except ValueError as e:
        print("Invalid input! Please enter an integer (Month 1-12).")
