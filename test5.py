# -*- coding: UTF-8 -*-
lis = [56,12,1,8,354,10,100,34,56,23,456,234,-58]
#冒泡排序
def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
        print lis
    return lis
s = sortport()
print s
#计算x的n次方
def power(x,n):
    s = 1
    while n>0:
        n= n-1
        s = s*x
    return s
def power1(x,n):
    s = x**n
    return s
result = power(1,5)
result1 = power1(1,5)
print result,result1
#计算a*a+b*b+c*c
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
#计算n的阶乘
def fac():
    num = int(input("请输入一个数字： "))
    factorial = 1
    if num < 0:
        print ("抱歉，负数没有阶乘")
    elif num == 0:
        print ("0的阶乘为1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print ("%d的阶乘为%d"%(num,factorial))
def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)
#列出当前目录下所有的文件和目录名
import os
files = [d for d in os.listdir('.')]
print files
#把一个list中的所有的字符串变为小写
L = ['Hello','Woels','sESdf']
str = [s.lower() for s in L]
print str
#输出某个路径下所有的文件和文件夹路径
def print_dir():
    filepath = ""
    if filepath == "":
        print ("请输入正确的路径")
    else:
        for i in os.listdir(filepath):  #获取目录中的文件及子目录列表
            print (os.path.join(filepath,i))  #把路径组合起来
print (print_dir())
#输出某个路径及其子目录下的所有文件路径
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        print path
        if os.path.isdir(path):
            show_dir(path)
filepath = "C:\Program Files\Internet Explorer"
print (show_dir(filepath))
#输出某个路径下及其子目录下所有以.html为后缀的文件
def print_dir(filepath):
    for i in (os.listdir(filepath)):
        path = os.path.join(filepath,i)
        if os.path.isdir(path):
            print_dir(path)
        if path.endswith(".html"):
            print path
filepath = "D:\\caseManage\\caseManage\\main\\templates"
print_dir(filepath)
# 把源字典的键值对颠倒生成字典
dict1 = {"A": "a","B":"b","C":"c"}
dict2 = {y:x for x,y in dict1.items()}
print dict2
for i in range(1,10):
    for j in range(1,i+1):
        print ('%d x %d = %d \t'%(i,j,i*j))
#替换列表中所有的3为3a
num = ["harden","lampard",3,34,45,56,76,87,45,3,3,3,454,34,23]
for i in range(num.count(3)):
    ele_index = num.index(3)
    num[ele_index]="3a"
print num
#合并去重
list1 = [2,3,8,4,9,5,6]
list2 = [5,6,10.17,11,2]
list3 = list1 +list2
print (list3)
print (set(list3))
print (list(set(list3)))