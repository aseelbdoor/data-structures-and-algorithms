
import math
def insertShiftArray(list,n):
    location=math.ceil(len(list)/2)
    newList=[]
    for i in range(0,len(list)):
        if i==location:
            newList.append(n)
        newList.append(list[i])
    else:
        if (len(newList)-1)<location:
            newList.append(n)
    return newList

#main
list1=[2,4,6,-8]
list2=[42,8,15,23,42]
list3=[1]
print(insertShiftArray(list3,2))
