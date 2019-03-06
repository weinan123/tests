# -*- coding: UTF-8 -*-
def quicksort(myList,start,end):
    if start < end :
        i,j = start,end
        #设置基准数
        base = myList[i]
        while i<j:
            #如果列表中后面的数，比基准数大或者相等，则前移一位直到有比基准数小的数出现
            while (i<j) and(myList[j] >= base) :
                j = j -1
            #如找到，则把第j个元素赋值给元素i,此时表中i,j
            myList[i] = myList[j]
            #同样的方式比较前半区
            while (i<j) and (myList[i] <= base):
                i = i+1
            myList[j] = myList[i]
        #做完第一轮之后，类表被分为了两个半区，并且i=j,需要将这个书设置回base
        myList[i] = base
        #递归前后半区
        quicksort(myList,start,i-1)
        quicksort(myList, j+1, end)
    return myList

myList = [49,38,65,97,76,13,27,67]
print ("quick sort")
quicksort(myList,0,len(myList)-1)
print (myList)



