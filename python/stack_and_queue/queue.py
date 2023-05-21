class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue(self,value) :
        """
        Adds a new element to the back of the queue.

        Args:
            value: The value to be added.

        Returns:
            None
        """
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
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The value of the element removed.

        Raises:
            Exception: If the queue is empty.
        """
        #check if queue is empty:
        if not self.front and not self.back:
            raise Exception("There is nothing to remove in this queue")
        #if not:
        elif self.front:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        elif self.back:
            self.back=None
            raise Exception("There is nothing to remove in this queue")
    
    def peek(self):
        """
        Returns the value of the element at the front of the queue without removing it.

        Returns:
            The value of the element at the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if not self.front:
            raise Exception("This queue dose not have front node")
        return self.front.value
    
    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        if not self.front:
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
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
