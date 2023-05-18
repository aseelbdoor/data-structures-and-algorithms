class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
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
        #check if the statck is empty :
        if not self.top:
            return "There is nothing to remove in the stack"
        temp= self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.top:
            return "This stake is empty so there is no top on it"
        return self.top.value
    def is_empty(self):
        #check if stack is empty-> True 
        #if not -> False
        if not self.top:
            return True
        return False

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    


if __name__ ==  "__main__":
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print(stack_01)
    stack_02= Stack()
    print(stack_02.pop())
    print(stack_02.is_empty())
    stack_01.pop()
    print(stack_01.peek())