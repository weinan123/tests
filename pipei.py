# -*- coding: UTF-8 -*-
#正则匹配
import re
#re.match只匹配字符串的开始。如果字符串开始不符合正则表达式，则正则匹配失败
print (re.match('aaa','aaaab').group())#在起始位置匹配
print (re.match('aaa','abbaaab'))#不在起始位置匹配，返回None
#re.search扫描整个字符串并返回第一个成功的匹配
print (re.search('haha','geihahanizhanggongzi').group())
#re.findall从左到右扫描字符串，按顺序返回匹配，如果无匹配则返回空列表
print (re.findall('\d','queshihenlihai'))
print (re.findall('\d','zhengchangfasheng'))
#sub用于替换字符串中的匹配项
print (re.sub('g..t','good','good geet up'))
#split返回切割后的列表
print (re.split('\+','123+456*789+abcd'))