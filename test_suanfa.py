# -*- coding: UTF-8 -*-
from __future__ import print_function
#冒泡排序
def bobble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
lists = [3,34,56,78,3,24,45]
print (bobble_sort(lists))
#计算X的n次方
def cal_xn(x,n):
    if n==1:
        return x
    else:
        return x**n
print (cal_xn(2,4))

#计算a*a+b*b+c*c
sum = 0
def cal_xn2(list,sum=0):
    for i in range(0,len(list)):
        sum = list[i]*list[i]+sum
    return sum
print (cal_xn2([1,2,3,6]))
#计算阶乘n
def cal_xn3(n):
    if n==1:
        return n
    else:
        return n*cal_xn3(n-1)
print (cal_xn3(5))
#列出当前目录下所有的文件及目录名
import os
#获得当前文件夹路径
path = os.getcwd()
print (path)
print (os.listdir("."))
#将一个列表中所有的字符串变成小写
list = ['A','WDWE','DSWDWsw']
list1 = [s.lower() for  s in list]
print (list1)
#输出某个路径下的所有文件及文件夹路径
def path_list(path):
    for i in os.listdir(path):
        print (os.path.join(path,i))
path_list(path)

#打印九九乘法表
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            if i==j:
                print("%d x %d=%d \t" % (i, j, i * j))
            else:
                print ("%d x %d=%d \t"%(i,j,i*j),end='')
jiujiu()
#替换列表中的3为3a
list2 = ['3',3,3,'3s3',333]
print (list2.count(3))
print(list2.index(3))
#修改之后在重新查找写入
for i in range(list2.count(3)): #获取3出现的次数
    #list2已变
    ele_index = list2.index(3)      #获取首次3出现的坐标
    list2[ele_index]="3a"           #修改3为3
    print(list2)
#打印每个名字
#合并去重
list3 = [1,'s','34',34,445,546]
list4 = ['ss','qqeweq','s',1,34,'wewerw']
list5 = list3+list4
print(list5)
list6 =set(list5)  #去重需重新转化为列表
#随机生成验证码的两种方式
import random
list7 = []
for i in range(0,9):
    list7.append(chr(i))
ma = random.sample(list7,5) #多个字符串选取特定数量的字符
mas = ''.join(ma)
print(mas)
#计算平方根
#判断字符串是否只有数字组成
import unicodedata
char = '121qqeqe'
print(char.isdigit()) #检测字符串是否由数字组成
#print(unicodedata.numeric(char))
#判断奇偶数
def is_jo(num):
    if(num % 2 == 0):
        #format字符串格式化参数
        print('{0}是偶数'.format(num))
    else:
        print('{0}是奇数'.format(num))
is_jo(89)
#判断闰年
def is_runYear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print('{0}是闰年'.format(year))
    else:
        print('{0}不是闰年'.format(year))
is_runYear(2016)
#获得最大值

#0，1，1，2，3
list7 = []
def fnbo_list(step):
    num1 = 0
    num2 = 1
    conut = 0
    print(num1,num2,end=' ')
    while conut < step:
        print(num1+num2,end=" ")
        num1,num2 = num2,num1+num2
        conut += 1
fnbo_list(9)
#十进制转二进制，八进制，十六进制
nums = 1313131313
print("十进制：",nums)
print("二进制为：",bin(nums))
print("八进制为：",oct(nums))
print("十六进制为：",hex(nums))
#最大公约数
def nax_gy(gy_nums1,gy_nums2):
    if gy_nums1 > gy_nums2:
        smaller = gy_nums2
    else:
        smaller = gy_nums1
    for i in range(1,smaller):
        if (gy_nums1 % i) == 0 and (gy_nums2 % i) == 0 :
            hcfs = i
    return hcfs
sss = nax_gy(8,12)
print(sss)
#最小公倍数
def nax_gb(gb_nums1,gb_nums2):
    if gb_nums1 > gb_nums2:
        greater = gb_nums1
    else:
        greater = gb_nums2
    while(True):
        if (greater % gb_nums1) == 0 and (greater % gb_nums2) == 0:
            lcm = greater
            break
        greater  +=1
    return lcm
lll = nax_gb(8,12)
print(lll)
#文件io
#写文件
'''
with open('test.txt',"rt") as f:
    f.write("写入啦哈哈哈")
with open("test.txt","wt") as f:
    f.read(u"读取了哈哈哈哈")
'''
#字符串判断
strS = 'ee2e3e23e'
strS.isalnum()   #数组或者字母
strS.isalpha()   #字母
strS.isdigit()   #数字
strS.islower()   #小写
strS.isupper()   #大写
strS.istitle()   #首字母大写
strS.isspace()   #空白字符
#字符串大小写转换
strS.upper()    #所有大写
strS.lower()    #所有小写
strS.capitalize() #首字母大写
strS.title()    #每个单词首字母大写
#list负数索引
listL = ["wo","ai","ni","men"]
print(listL[-1])
#list增加元素
listL.append("6666")
print(listL)
listL.insert(5,"123")
print(listL)
listL.extend(["weinan","jiayou"])
#list搜索元素
eleS = listL.index("weinan")
print(eleS)
#list删除元素
listL.pop()   #删除最后一个元素并返回该值
print(listL)
listL.pop(-1)
print(listL)
listL.remove("123") #删除首次出现该元素的值
#list变为字符串
strT = "".join(listL)
print(strT)
#list分割字符串
strP = strT.split("n")
print(strP)
#字典解析
parmas = {"name":"zhangsan","age":18,"sex":"girl"}
print(parmas.keys())
print(parmas.values())
print (parmas.items())
#列表生成式
listW = [ele for ele in listL if ele=="wo"]
print (listW)
str67 = "123456789"
numqew = random.choice(str67)
djskdjwe = random.sample(str67,8)
swrw = ''.join(djskdjwe)
print(numqew,djskdjwe,swrw)