
import math
def BinarySearch(list,a):
    low=0
    high=len(list)-1
    while low<=high:
        mid=math.floor((low+high)//2)
        if list[mid]==a:
           return mid
        elif list[mid]>a:
            high=mid
        else:
            low=mid+1
    else:
        return -1

#main 
list1=[4,8,15,16,23,42]

list2=[-131,-82,0,27,42,68,179]
list3=[11,22,33,44,55,66,77]
list4=[1,2,3,5,6,7]
print(BinarySearch(list1,15))
print(BinarySearch(list2,42))
print(BinarySearch(list3,90))
print(BinarySearch(list4,4))