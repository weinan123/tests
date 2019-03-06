# -*- coding: UTF-8 -*-
#高阶函数
f = abs     #函数本身可以赋值给变量
print f(-10)
''' 函数接收另外一个函数作为参数，称为高阶函数'''
def add(x,y,f):
    return f(x)+f(y)
result = add(-5,-6,abs)
print result
#map
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7])
print list(r)
#capitalize()首字母大写，其他字母小写
def normalize(name):
    return name.capitalize()
L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print L2
def prod(L):
    return reduce(lambda x,y:x*y,L)
str = prod([3,5,7,9])
print str
#filter
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n <1000:
        print n
    else:
        break
def is_palindrome(n):
    return n and n == reversed(n)
listsqwe = list(filter(is_palindrome,[123,121,345,23432]))
print listsqwe
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()