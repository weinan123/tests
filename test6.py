# -*- coding: UTF-8 -*-
#随机生成验证码的两种方式
import random,string
list1 = []
for i in range(65,91):
    list1.append(chr(i))
for j in range(97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))
#random.sample从序列中选择n个随机且独立的元素
ma = random.sample(list1,6)
print ma
#列表变为字符串
ma = ''.join(ma)
print ma

str1 = "0123456789"
str2 = string.ascii_letters    #包含所有字母大小写的字符串
str3 = str1+str2
mal = random.sample(str3,6)
mal = "".join(mal)
print (mal)
#计算平方根
num = float(input("请输入一个数字："))
num_sqrt = num**0.5
print num_sqrt
#判断字符串是否只有数据组成
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
#计算闰年。非整百且能被4整除的是闰年，整百能被四百整除的是闰年
year = int(input("请输入一个年份:"))
if (year % 4) == 0:
    if (year % 100)== 0:
        if (year % 400)==0:
            print ("{ 0 }是闰年".format(year))
        else:
            print ("{ 0 }不是闰年".format(year))
    else:
        print ("{ 0 }是闰年".format(year))
else:
    print ("%d是闰年"%(year))
#判断是否是闰年
year = int(input("请输入一个年份："))
if (year % 4)==0 and (year % 400)==0 and (year % 100)!=0:
    print ("%d是闰年"%(year))
else:
    print ("%d不是闰年" % (year))
#获取最大值
n = int(input("请输入需要对比数字的个数"))
print ("请输入需要对比的数字")
num = []
for i in range(1,n+1):
    temp = int(input("输入第%d个数字"% i))
    num.append(temp)
print ("您输入的数字为：",num)
print ("最大值为：",max(num))
#list的常见操作
list = [1,2,3,4,6,7,7]
print list[-1]
print list[1:3]
list.append("new")
list.insert(2,"new")
list.extend([123,345])
list.index("new")
list.remove("c")
list.pop()   #删除最后一个元素，并返回元素的值
list = list + ["haha","dhwidh"]
list = ["123","2312"]*3
#使用join链接list成为字符串
print ("".join(list))
#list分割字符串
s = "1313113"
s.split(";")
s.split(";",1) #只分割第一个分号
#list的映射关系
li = [1,5,7,5]
s = [elem *2 for elem in li]
#字典中的解析
params = {"father":"yibing","mather":"weinan","childern":"weiyiyi"}
keys = params.keys()
values = params.values()
items = params.items()
key = [k for k,v in params.items()]
value = [v for k,v in params.items()]
item = ["%s=%s" % (k,v) for k,v in params.items()]