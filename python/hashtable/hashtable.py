from functools import reduce
from operator import add

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value


class LinkedList:
  '''
  what : A class representing a singly linked list data structure
  '''
  def __init__(self):
    self.head = None


  def insert (self, value):
    '''
    insert a new node with the given value at the begining of     the linked list.
    args: value
    output : none
    '''
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node


class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    self.repeat=[]
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
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
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''
    if self.get(key):
      return True
    return False  

    
  def keys(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys
  
  def repeated_word(self,string):
    """
        Find the first word that occurs more than once in the given string.

        Parameters:
            string (str): The input string to search for repeated words.

        Returns:
            str: A string describing the first word that occurred more than once
                 and the number of times it was repeated.
        Raises:
            Exception: If the input string is empty (contains no words).
    """
    string=string.strip().lower().split()
    if len(string)==0:
      raise Exception("There is no words in this string")
    cou=0 
    for key in string:
      key=key.strip(',').strip('.').strip('!').strip('?')
      index = self.__hash(key)
      if self.__buckets[index] is None:
        ll = LinkedList()
        self.__buckets[index] = ll
        self.__buckets[index].insert([key,1])
      else:
        curr = self.__buckets[index].head
        while curr :
          if curr.value[0] == key:
            if cou==0:
              cou+=1
              self.repeat=curr.value
            curr.value[1]=curr.value[1]+1
          curr = curr.next  
      self.keys.append(key)
    return f'The first word to occur more than once in this string is ({self.repeat[0]}) that repeated : {self.repeat[1]} times'