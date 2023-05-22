
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
    def __init__(self,head=None):
        self.head=head

    def __str__(self):
        return f"Hi I am the Linked List my value is {self.head.value} and the next node after me is {self.head.next.value}"
    
    def zipLists(self, other):
        """
        Merges two linked lists by alternating their elements.

        Parameters:
            self (LinkedList): The first linked list.
            other (LinkedList): The second linked list.

        Returns:
            Node: The head node of the merged linked list.

        Raises:
            Exception: If both linked lists are empty.

        Description:
            This method merges two linked lists by alternating their elements.
            The elements from the first linked list are appended first, followed by the elements from the second linked list.
            The merged linked list is created and returned as a new linked list.
        """
        if not self.head and not other.head:
            raise Exception("You can not merge two empty lists")
        temp=[]
        current1=self.head
        current2=other.head
        if not current1:
            self.head=other.head
        while current1 or current2:
            if current1:
                temp.append(current1)
                current1=current1.next
            if current2:
                temp.append(current2)
                current2=current2.next
        for i in range(0,len(temp)-1):
            temp[i].next=temp[i+1]
        return self.head
            
    def to_string(self):
        """
        Converts the linked list to a string representation.

        Returns:
            str: The string representation of the linked list.

        Description:
            This method traverses the linked list and constructs a string representation of its elements.
            The elements are enclosed in curly braces and separated by arrows "->".
            The string representation is returned.
        """
        a=""
        current=self.head
        while current:
            a=a+"{"+str(current.value)+"} "
            a+="-> "
            current = current.next
        a+="Null"
        return a
    
if __name__=="__main__":
    nodel1=Node(2)
    nodel2=Node(3,nodel1)
    nodel3=Node(1,nodel2)
    list1=LinkedList(nodel3)
    print(list1.to_string())
    nodeli1=Node(4)
    nodeli2=Node(9,nodeli1)
    nodeli3=Node(5,nodeli2)
    list2=LinkedList(nodeli3)
    print(list2.to_string())
    list1.zipLists(list2)
    print(list1.to_string())
