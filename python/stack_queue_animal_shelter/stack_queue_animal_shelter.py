
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
            string+=f"{current.value.name}"
            string+=" -> "
            current=current.next
        return string+"None"    


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class AnimalShelter:
    def __init__(self,first=None):
        self.first=first
        self.second=Stack()
    
    def enqueue(self,animal):
        """
        Adds an animal to the queue.

        Parameters:
            self (Queue): The Queue object.
            animal: The animal object to be added to the queue.

        Returns:
            None
        """
        self.first.push(animal)

    def dequeue(self,pref):
        """
        Removes and returns an element from the queue based on the specified preference.

        Parameters:
            self (Queue): The Queue object.
            pref (str): The preferred species ("cat" or "dog") for removing an element.

        Returns:
            str: The species of the removed element, or "Null" if no element matching the preference is found.

        Raises:
            Exception: If the queue is empty and there is nothing to remove
        """
        if pref not in ["cat","dog"]:
            return "Null"
        current=self.first.top
        if not current:
            raise Exception("The queue is empty nothing to remove")
        while current:
            self.second.push(current.value)
            self.first.pop()
            current=self.first.top
        temp=""
        current=self.second.top
        counter=0
        while current:
            if current.value.species==pref and counter==0 :
                temp=self.second.pop()
                counter+=1
            else:
                self.first.push(current.value)
                self.second.pop()
            current=self.second.top
        if temp=="":
            return "Null"
        return temp.species

#main
an1=Animal("hackey","dog")
an2=Animal("lisa","cat")
an3=Animal("lolo","dog")
an4=Animal("jojo","cat")
stack1=Stack()
queue1=AnimalShelter(stack1)
queue1.enqueue(an1)
queue1.enqueue(an2)
queue1.enqueue(an3)
queue1.enqueue(an4)
print(stack1)
print(queue1.dequeue("cat"))
print(stack1)