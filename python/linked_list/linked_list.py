import math
class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
    def __str__(self) -> str:
        if self.next==None:
            return f"Hi I am {self.value} the last node"
        else:
            return f"Hi I am {self.value} the next node after me is {self.next.value}"
        

class LinkedList:
    head=None
    def __init__(self,head=None):
        self.head=head
        LinkedList.head=head

    def __str__(self):
        if self.head==LinkedList.head:
            return f"Hi I am the Linked List my value is {self.head.value} and the next node after me is {self.head.next.value}"
        else:
            return f"Hi I am {self.head.value} the next node after me is {self.head.next.value}"
    @classmethod
    def includes(cls,value):
        current=cls.head
        while current:
            if current.value==value:
                return True
            current=current.next
        return False
    @classmethod
    def to_string(cls):
        a=""
        current=cls.head
        while current:
            a=a+"{"+str(current.value)+"} "
            a+="-> "
            current = current.next
        a+="Null"
        return a
    
    @classmethod
    def insert(cls,value):
        node=Node(value)
        if cls.head==None:
            print("You should be have Head for the linked list")
            return 
        node.next=cls.head
        cls.head=node
        return node

    @classmethod
    def traverse(cls) :
        if cls.head==None:
            print("You should be have Head for the linked list")
            return 
        linkedlist=[]
        current = cls.head
        while current:
            linkedlist.append(current.value)
            current = current.next
        return linkedlist
    
    @classmethod
    def append(cls,value):
        node = Node(value)
        if cls.head==None:
            cls.head = node
        else:
            current = cls.head
            while current.next:
                current = current.next
            current.next = node
        return node

    @classmethod
    def insert_before(cls,value,newValue):
        if cls.head==None:
            print("You should be have Head for the linked list")
            return 
        if value==None:
            cls.append(newValue)
            return
        befCurrent=None
        current = cls.head
        while current:
            if current.value==value:
                if befCurrent==None:
                    cls.insert(newValue)
                    return
                else:
                    node=Node(newValue)
                    befCurrent.next=node
                    node.next=current
                    return

            befCurrent=current
            current=current.next
        print(f"No change there is no node with value {value}")
    
    @classmethod
    def insert_after(cls,value,newValue):
        if value==None:
            print("You can not insert value after nothing")
            return
        if cls.head==None:
            print("You should be have Head for the linked list")
            return 
        current = cls.head
        aftCurrent=current.next
        node=Node(newValue)
        while current:
            if current.value==value:
                node.next=aftCurrent
                current.next=node
                return
            current=current.next
            aftCurrent=current.next
        print(f"No change there is no node with value {value}")
    @classmethod
    def length(cls):
        counter=0
        current=cls.head
        while current:
            counter+=1
            current=current.next
        return counter
    
    @classmethod
    def kthFromEnd(cls,k):
        length=cls.length()
        if k>=0 and k<length:
            current=cls.head
            location=length-k
            for i in range(1,location):
                current=current.next
            else:
                return current.value
        elif k<0 and abs(k)<=length:
            current=cls.head
            location=-k
            for i in range(1,location):
                current=current.next
            else:
                return current.value
        return "This place does not exist in this Linked List"
    
    @classmethod
    def middle(cls):
        middle=math.ceil(cls.length()/2)
        current=cls.head
        for i in range(1,middle):
            current=current.next
        return current.value

if __name__=="__main__":
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    LinkedList.append(4)
    print(LinkedList.to_string())
    print(LinkedList.kthFromEnd(8))
    print(LinkedList.middle())