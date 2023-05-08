def SequentialSearch(list,a):
    for i in range(0,len(list)):
        if list[i]==a:
            return i
    return -1

#main 
list1=[4,8,15,16,23,42]
list2=[-131,-82,0,27,42,68,179]
list3=[11,22,33,44,55,66,77]
list4=[1,2,3,4,5,6,7]
print(SequentialSearch(list2,0))
