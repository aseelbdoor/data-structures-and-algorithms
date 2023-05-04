import math
def insertShiftArray(list,n):
    location=math.ceil(len(list)/2)
    newList=[]
    for i in range(0,len(list)):
        if i==location:
            newList.append(n)
        newList.append(list[i])
    return newList

#main
list1=[2,4,6,-8]
list2=[42,8,15,23,42]
print(insertShiftArray(list2,16))