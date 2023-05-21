import pytest
from python.stack_and_queue.stack import Stack
from python.stack_and_queue.queue import Queue

def test_push():
    stack=Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    actual=str(stack)
    expected="3 -> 4 -> 5 -> None"
    assert actual==expected

def test_pop():
    stack=Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    with pytest.raises(Exception):
        stack.pop()

def test_peek():
    stack=Stack()
    with pytest.raises(Exception):
        stack.peek()
    stack.push(5)
    actual2=stack.peek()
    expected2=5
    assert actual2==expected2

def test_enqueue():
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    actual=str(q)
    expected="hi -> welcome -> bye -> None"
    assert actual== expected

def test_dequeue():
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    with pytest.raises(Exception):
        q.dequeue()

def test_queue_peek():
    q=Queue()
    with pytest.raises(Exception):
        q.peek()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    actual2=q.peek()
    expected2="hi"
    assert actual2==expected2

