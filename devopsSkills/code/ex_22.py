while True:
    try:
        str_input = input("Nhap diem toan van anh: ")
        toan , van, anh = map(float, str_input.split())

        if not (0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10):
                print("Loi: Diem phai nam trong khoang 0 - 10.")
                continue

        tb = (toan+van+anh)/3

        if tb >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5 and ( toan >= 8 or van >= 8)  :
            print("Hoc sinh gioi")
        elif tb >= 6.5 and toan >= 5 and van >= 5 and anh >= 5 and ( toan >= 6.5 or van >= 6.5):
            print("Hoc sinh kha")
        elif tb >= 5 and toan >= 3.5 and van >= 3.5 and anh >= 3.5 and ( toan >= 5 or van >= 5):
            print("Hoc sinh trung binh")
        elif tb >= 3.5 and toan >= 2 and van >= 2 and anh >= 2 and ( toan >= 3.5 or van >= 3.5):
            print("Hoc sinh yeu")
        else:
            print("hoc sinh kem")        
    
    except ValueError:
        print("Please enter an integer")
