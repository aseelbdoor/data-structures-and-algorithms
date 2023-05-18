class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue(self,value) :
        node = Node(value)
        #check if queue is empty:
        if not self.front and not self.back:
            self.front=node
            self.back=node
        elif not self.back:
            self.back=node
            self.front.next=node
        # if not :
        else:
            self.back.next= node
            self.back = node 

    def dequeue(self):
        #check if queue is empty:
        if not self.front and not self.back:
            return "There is nothing to remove in this queue"
        #if not:
        elif self.front:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        elif self.back:
            self.back=None
            return "There is nothing to remove in this queue"
    
    def peek(self):
        if not self.front:
            return "This queue dose not have front node"
        return self.front.value
    
    def is_empty(self):
        if not self.front:
            return True
        return False

    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"   


if __name__ == "__main__":
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    # print("deleted element is ",q.dequeue())#deleted node value
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.back.value)
    print(q)
