# -*- coding: UTF-8 -*-
import math
#转义\
print ('I\'m ok.')
#\n换行符\t制表符
print ('I\'m learnning\npython')
#r''内部字符串默认不转义
print (r'\n\t\123')
#'''...'''表示多行内容
print (r'''123,\n
wer
23123
313123''')
print (not True)
#list有序集合，可以随时添加和删除其中的元素
classmate = ['bob','alice','jim']
classmate.append('weinannan')
classmate.insert(1,'yiyi')
#删除末尾元素
classmate.pop(1)
print classmate
#tuple()有序列表叫元组，一旦初始化不能修改
L = [
    ['apple','goole','microsoft'],
    ['java','python','ruby','php'],
    ['adam','bart','lisa']
]
print L[0][0]
print L[1][1]
print L[2][2]
height = 1.67
weight = 58
bmi = weight/(height**2)
print bmi
if bmi<18.5:
    print "过轻"
elif 18.5<= bmi< 25:
    print "正常"
elif 25<= bmi< 28:
    print "过重"
elif 28<= bmi< 32:
    print "肥胖"
elif bmi> 32:
    print "严重肥胖"
L = ['yibing','weinan','weiyiyi']
for i in L:
    print 'hello '+i +'\n'
#dict的用法
#set与dict类似。是一种key的集合，但是不存贮value
s = set([1,1,4,2,2,3])
s.remove(4)
print s
#str 数字不可变对象 list是可变对象
n1 = 255
n2 = 1000
print (hex(n1))
import math
def quadratic(a,b,c):
    isHave = b**2-4*a*c
    if isHave>=0:
        result1 = -b+math.sqrt(isHave)/2*a
        result2 = -b-math.sqrt(isHave)/2*a
        return result1, result2
    elif isHave<0:
        print "无解"
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#默认参数，可变参数，关键字参数
#默认参数必须指向不可变对象str,None
#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n*n
    return sum
nums = [1,2,3]
print calc(*nums)
#关键字参数
def person(name,age,**kw):
    print name,age,kw
extra = {'city':'beijing','job':'teacher'}
print person("zhangsan",'30',**extra)
#命名关键字参数，限制关键字参数的名字

def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n - 1, a, c, b)  # 有n个盘子，借助于C，A(n-1) --> B
        move(1, a, b, c)  # 有n个盘子，A(1) --> C
        move(n - 1, b, a, c)  # 有n个盘子，借助于A，B(n-1) --> C

move(5,"A","B","C")
#迭代dict for k,v in d.items
def findMinAndMax(L):

    if L==[]:
        return (None,None)
    else:
        maxL = L[0]
        minL = L[0]
        for i in range(1,len(L)):
            maxL = max(L[i],maxL)
            minL = min(L[i],minL)
        return (maxL,minL)

result1 = findMinAndMax([])
result2 = findMinAndMax([7])
result3 = findMinAndMax([7, 1])
result4 =findMinAndMax([7, 1, 3, 9, 5])
print result1,result2,result3,result4
#列表生成式
list = [m+n for m in 'ABC' for n in "XYZ"]
print list
L1 = ['Hello','World',18,'Apple',None]
L = [s.lower() for s in L1 if isinstance(s,str)==True]
print L
#生成器
def triangles():
    s = [1]
    print s
    yield
    s2=[1,1]
    print s2
    yield
    s3 = [1]
    for i in range(0,len(s2)):
        if i +1<len(s2):
            cas = s2[i]+s2[i+1]
            s3.append(cas)
        else:
            break
    s3.append(1)
    print s3
    yield
o = triangles()
next(o)
next(o)
next(o)
#迭代器，可迭代对象
'''
list,dict,str等都是迭代对象不是迭代器，可以使用iter()函数获取一个迭代器对象，python的for循环是一个迭代器
'''








