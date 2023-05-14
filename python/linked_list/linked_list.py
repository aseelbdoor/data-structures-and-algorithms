
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
    head=''
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
            a=a+"{"+current.value+"} "
            a+="-> "
            current = current.next
        a+="Null"
        return a
    
    @classmethod
    def insert(cls,value):
        node=Node(value)
        node.next=cls.head
        cls.head=node

    @classmethod
    def traverse(cls) :
        linkedlist=[]
        current = cls.head
        while current:
            linkedlist.append(current.value)
            current = current.next
        return linkedlist
        
    

if __name__=="__main__":
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.insert("Aseel")
    print(LinkedList.traverse())
    print(LinkedList.to_string())
    print(LinkedList.includes("raya"))
    print(node_d)
    print(11,LinkedList.head)