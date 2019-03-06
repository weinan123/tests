# -*- coding: UTF-8 -*-
a = b = c =1
a,b,c = 1,2,"nan"
print a,b,c
a,b = b,a
print a,b
file_path = 'C:\Users\\nan.wei\\Desktop\\666.txt'
fp = open(file_path,'r+')
str = fp.read()
print (str)
position = fp.tell()
print (u"当前位置",position)
position = fp.seek(0,0)
str = fp.read(2)
print (u"文件中的内容为",str)
#关闭打开的文件夹
fp.close()
#write
filewrite = open(file_path,"w")
filewrite.write("weinannan haokeai")
filewrite.close()
#wirtelines
filewrite1 = open(file_path,"r+")
filewrite1.writelines(["daydayup\n","learnlearnstart"])
filewrite1.close()
#在不关闭文件的情况下读取文件的内容
filewrite2 = open(file_path,"r+")
filewrite2.write("newdaydayup")
#把光标定位到开始，读取全部文件内容
filewrite2.seek(0,0)
str = filewrite2.read()
print str
#把光标定位到文件末尾，打印有多少个字符
s = filewrite2.seek(0,2)
print s
#删除
filewrite2.seek(0,0)
#filewrite2.truncate(2)
#filewrite2.truncate()
filewrite2.close()