# -*- coding: UTF-8 -*-
list = [3,5,8,2,4,6,7]
def bubble_sort():
    for i in range(0,len(list)-1):
        #i是控制循环的次数.j是比较数据的个数的下标
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
newlist =bubble_sort()
print newlist
print list[::-1]
#快速排序
'''
1.从列表中挑出一个元素。作为基准值key
2.所有小于key的元素放左边，大于key的元素放右边
3.递归左侧列表和右侧列表

'''
def quick_sort(lists,left,right):
    if left >=right:
        return lists
    #定义游标
    low = left
    high = right
    base = lists[low]
    while low < high:
        while low < high and lists[high] >= base:
            high = high-1
        lists[low] = lists[high]
        while low < high and lists[low] < base:
            low = low+1
        lists[high] = lists[low]

    lists[high] = base
    print lists
    quick_sort(lists,left,low-1)
    quick_sort(lists,high+1,right)
    return lists
mylist = [5,10,88,19,9,1,7]
print (quick_sort(mylist,0,6))
'''
二分查找，先排序再查找
'''
def binayr_search(arr,start,end,hkey):
    if start > end:
        return -1
    mid = start+(end-start)/2
    if arr[mid] > hkey:
        return binayr_search(arr,start,mid-1,hkey)
    if arr[mid] < hkey:
        return binayr_search(arr,mid+1,end,hkey)
    return mid



