import pytest
from python.stack_queue_pseudo.stack_queue_pseudo import Node,Stack,pseudo_queue

def test_enqueue():
    node1=Node("aseel")
    stack1=Stack(node1)
    queue1=pseudo_queue(stack1)
    queue1.enqueue("bdoor")
    actual=str(queue1)
    expected="bdoor -> aseel -> None"
    assert actual == expected

def test_dequeue():
    node1=Node("aseel")
    stack1=Stack(node1)
    queue1=pseudo_queue(stack1)
    queue1.enqueue("bdoor")
    actual=queue1.dequeue()
    expected="aseel"
    stack2=Stack()
    queue2=pseudo_queue(stack2)
    with pytest.raises(Exception):
        queue2.dequeue()
    assert actual == expected
