import math
def removes(list):
    location=math.floor(len(list)/2)
    newList=[]
    for i in range(0,len(list)):
        if i==location:
            continue
        else:
            newList.append(list[i])
    return newList

#main
list1=[2,4,6,-8]
list2=[42,8,15,23,42]
list3=[]
print(removes(list1))