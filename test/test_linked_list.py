import pytest
from python.linked_list.linked_list import Node,LinkedList

def test_node():
    node_d=Node ("Alaa")
    actual1 = str(node_d)
    expected1 = "Hi I am Alaa the last node"
    node_H=Node ("Haneen",node_d)
    actual2 = str(node_H)
    expected2 = "Hi I am Haneen the next node after me is Alaa"
    assert actual1 == expected1 and actual2==expected2

def test_linked_list():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    actual=str(ll)
    excepted="Hi I am the Linked List my value is Haneen and the next node after me is Alaa"
    assert actual==excepted

def test_include():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    actual1=LinkedList.includes("Aseel")
    actual2=LinkedList.includes("Haneen")
    expected1=False
    expected2=True
    assert actual1==expected1 and actual2==expected2

def test_insert():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.insert("Aseel")
    actual=str(LinkedList.head)
    expected="Hi I am Aseel the next node after me is Haneen"
    assert actual== expected

def test_to_string():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    actual= LinkedList.to_string()
    expected="{Haneen} -> {Alaa} -> Null"
    assert actual==expected

def test_traverse():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.insert("Aseel")
    actual=LinkedList.traverse()
    expected=['Aseel', 'Haneen', 'Alaa']
    assert actual == expected

def test_append():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.append("Bdoor")
    a=LinkedList.append("Aseel")
    actual=str(a)
    expected="Hi I am Aseel the last node"
    assert actual==expected

def test_insert_before():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.append("Bdoor")
    LinkedList.append("Aseel")
    LinkedList.insert_before("Aseel","Leen")
    LinkedList.insert_before("Haneen","Haya")
    actual=LinkedList.to_string()
    expected="{Haya} -> {Haneen} -> {Alaa} -> {Bdoor} -> {Leen} -> {Aseel} -> Null"
    assert actual==expected

def test_insert_after():
    node_d=Node ("Alaa")
    node_H=Node ("Haneen",node_d)
    ll= LinkedList(node_H)
    LinkedList.append("Bdoor")
    LinkedList.append("Aseel")
    LinkedList.insert_after("Haneen","Maysaa")
    LinkedList.insert_after("Aseel","Haya")
    actual=LinkedList.to_string()
    expected="{Haneen} -> {Maysaa} -> {Alaa} -> {Bdoor} -> {Aseel} -> {Haya} -> Null"
    assert actual==expected

def test_kthFromEnd1():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(6)
    expected="This place does not exist in this Linked List"
    assert actual==expected

def test_kthFromEnd2():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(-1)
    expected=1
    assert actual==expected

def test_kthFromEnd3():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(0)
    expected=2
    assert actual==expected

def test_kthFromEnd4():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(-3)
    expected=8
    assert actual==expected

def test_kthFromEnd5():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(2)
    expected=3
    assert actual==expected

def test_kthFromEnd6():
    node_d=Node (8)
    node_H=Node (3,node_d)
    ll= LinkedList(node_H)
    LinkedList.append(2)
    LinkedList.insert(1)
    actual=LinkedList.kthFromEnd(4)
    expected="This place does not exist in this Linked List"
    assert actual==expected

def test_kthFromEnd7():
    node_d=Node (8)
    ll= LinkedList(node_d)
    actual1=LinkedList.kthFromEnd(0)
    actual2=LinkedList.kthFromEnd(-1)
    expected=8
    assert actual1==expected and actual2==expected
