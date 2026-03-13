# Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất

def nhap_dictionary():
    n = int(input("so phan tu muon nhap: "))
    mydict ={}

    for i in range (0,n):
        print(f"phan tu thu {i+1} :")
        key = input("nhap key: ")
        value = int(input("nhap gia tri cho key: "))
        mydict[key] = value

    print("gia tri dictionary la: ",mydict)
    return mydict

def tim_key_lon_nhat(mydict):
    maxValue = max(mydict, key=mydict.get)
    print("ket qua key lon nhat la: ",maxValue)

data =nhap_dictionary()

tim_key_lon_nhat(data)
