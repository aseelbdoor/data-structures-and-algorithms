class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        node = Node(value)
        #check if the statck is empty or not 
        # if its empty :
        if not self.top:
            self.top=node
        #IF NOT :
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        #check if the statck is empty :
        if not self.top:
            raise Exception("There is nothing to remove in the stack")
        temp= self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        Returns the value from the top of the stack without removing it.

        Returns:
            The value from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if not self.top:
            raise Exception("This stake is empty so there is no top on it")
        else:
            return self.top.value
        
    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        #check if stack is empty-> True 
        #if not -> False
        if not self.top:
            return True
        return False  
    
    def __str__(self):
        """
        Returns:
            A string representation of the stack, showing its elements from top to bottom.
        """
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    

class pseudo_queue:
    def __init__(self,first=None):
        self.first=first
        self.second=Stack()

    def __str__(self):
        """
        Returns a string representation of the queue
        """
        current=self.first.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None" 
      
    def enqueue(self,value):
        """
    Adds a new element to the queue.

    Parameters:
        value: The value to be added to the queue.

    Returns:
        None
        
    """
        if self.first.is_empty():
            node=Node(value)
        else:
            node=Node(value,self.first.top)
        self.first.top=node
    
    def dequeue(self):
        """
    Removes and returns the element at the front of the queue.

    Returns:
        The element at the front of the queue.

    Raises:
        Exception: If the queue is empty.

    """
        current=self.first.top
        if not current:
            raise Exception("The queue is empty nothing to remove")
        elif not current.next:
            temp=self.first.pop()
            return temp
        while current:
            self.second.push(current.value)
            self.first.pop()
            current=self.first.top
        temp=self.second.pop()
        current=self.second.top
        while current:
            self.first.push(current.value)
            self.second.pop()
            current=self.second.top
        return temp

#main
if __name__=="__main__":
    node1=Node("aseel")
    stack1=Stack(node1)
    queue1=pseudo_queue(stack1)
    queue1.enqueue("bdoor")
    print(queue1)
    print(queue1.dequeue())
    print(queue1)
    print(queue1.dequeue())
    print(queue1)