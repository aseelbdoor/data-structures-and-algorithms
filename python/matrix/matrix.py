
def matrix(a):
    newList=[]
    for i in a:
        counter=0
        for j in i:
            counter+=j
        newList.append(counter)
    return newList


list1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
list2=[[-1,-2,-3,-11],[-13,-14,-15]]
print(matrix(list2))