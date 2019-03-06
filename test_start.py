# -*- coding: UTF-8 -*-
def comBanben(banBen1,banBen2):
    banben1 = str(banBen1)
    banben2 = str(banBen2)
    bijiao1 = banben1.split(".")
    bijiao2 =banben2.split(".")
    print bijiao1,bijiao2
    data1 = []
    for i in range(0,len(bijiao1)):
        num = int(bijiao1[i])
        data1.append(num)
    data2 = []
    for i in range(0, len(bijiao2)):
        num = int(bijiao2[i])
        data2.append(num)
    print data1,data2
    jigguo = ""
    for i in range(0,len(data1)):
        if data1[i]>data2[i]:
            jigguo = "版本1大"
            break
        elif data1[i] == data2[i]:
            if i < len(data1)-1:
                i = i + 1
                continue
            else:
                jigguo = "版本一样大"
        elif data1[i] < data2[i]:
             jigguo = "版本2大"
             break
    return jigguo
jigguo1 = comBanben("1.3.3","1.3.3")
print jigguo1

def comBanben2(str1,str2):
    banben1 = str(str1)
    banben2 = str(str2)
    bijiao1 = banben1.split(".")
    bijiao2 =banben2.split(".")
    print bijiao1,bijiao2
    data1 = []
    for i in range(0,len(bijiao1)):
        num = int(bijiao1[i])
        data1.append(num)
    data2 = []
    for i in range(0, len(bijiao2)):
        num = int(bijiao2[i])
        data2.append(num)
    print data1,data2
    num = 0
    for i in range(0,len(data1)):
        num = num +data1[i]*(10**(len(data1)-1-i))
    print num
comBanben2("1.3.2","1.3.3")


