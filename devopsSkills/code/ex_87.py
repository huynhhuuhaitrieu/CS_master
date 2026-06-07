# Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên
# dương k. Hãy tạo và trả về một list L_kq có các phần tử là giá trị của
# phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần.
a = int(input("Nhap so nguyen duong K:  "))
mylist1 = list(map(int,input("Nhap gia tri list L:   ").split()))
# print(mylist)
def cac_phan_tu_xuat_hien_hon_K_lan(k,mylist):
    mydict = {}
    outlist =[]
    for i in range(0,len(mylist)):
        if mylist[i] not in mydict:
            mydict[mylist[i]]= 1
        else:
            mydict[mylist[i]]+= 1
    # for i in mydict.values():
    #     if i < k:
    #         del mydict[i]
    print(mydict)

    list1 = list(mydict.keys())
    print("list1: ",list1)

    for i in range(0,len(list1)):
        if mydict[list1[i]] > k:
            outlist.append(list1[i])

    print("outlist: ",outlist)
    outlist.sort()
    print("outlist: ",outlist)
    return outlist

cac_phan_tu_xuat_hien_hon_K_lan(a,mylist1)
