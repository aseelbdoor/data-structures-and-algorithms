from functools import reduce
from operator import add

class Node:
  def __init__(self, value):
      self.next=None 
      self.value=value


class LinkedList:
  def __init__(self):
    self.head = None


  def insert (self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node


class HashTable:
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    self.repeat=[]
    
  
  def __hash(self,key):
    key=str(key)
    return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

    
  def set(self,key,value):
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    

  def get(self,key):
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    

  def has(self, key):
    if self.get(key):
      return True
    return False  
  
  def keys(self):
    return self.keys
  
def left_join(ht1,ht2):
  keys1=ht1.keys()
  keys2=ht2.keys()
  baselist=[]
  for i in keys1:
    new=[i]
    new.append(ht1.get(i))
    if i in keys2:
      new.append(ht2.get(i))
    else:
      new.append(None)
    baselist.append(new)
  return baselist



if __name__=="__main__":
  pass