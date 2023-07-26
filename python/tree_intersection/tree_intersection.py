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

  
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None

class binaryTree:
  def __init__(self):
    self.root=None


def tree_intersection(tr1,tr2):
    if (tr1.root is None) or (tr2.root is None):
      raise Exception("There is no values found in both trees")
    ht=HashTable()
    arr=[]
    def _walk(root):
      if ht.has(root.value):
        arr.append(root.value)
      ht.set(root.value," ")
      if root.left :
        _walk(root.left)
      if root.right :
        _walk(root.right)
    _walk(tr1.root)
    _walk(tr2.root)
    if len(arr)==0:
      return "There is no values found in both trees"
    return arr
    
