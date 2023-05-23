import pytest
from python.ziplists.ziplists import Node,LinkedList,zipLists

def test_empty_tow_lists():
    list1=LinkedList()
    list2=LinkedList()
    with pytest.raises(Exception):
        list1.zipLists(list2)
        
def test_one_empty1():
    nodel1=Node(2)
    nodel2=Node(3,nodel1)
    nodel3=Node(1,nodel2)
    list1=LinkedList(nodel3)
    list2=LinkedList()
    zipLists(list1,list2)
    actual=list1.to_string()
    expected="{1} -> {3} -> {2} -> Null"
    assert actual==expected

def test_one_empty2():
    list1=LinkedList()
    nodeli1=Node(4)
    nodeli2=Node(9,nodeli1)
    nodeli3=Node(5,nodeli2)
    list2=LinkedList(nodeli3)
    zipLists(list1,list2)
    actual=list1.to_string()
    expected="{5} -> {9} -> {4} -> Null"
    assert actual==expected

def test_same_long():
    nodel1=Node(2)
    nodel2=Node(3,nodel1)
    nodel3=Node(1,nodel2)
    list1=LinkedList(nodel3)
    nodeli1=Node(4)
    nodeli2=Node(9,nodeli1)
    nodeli3=Node(5,nodeli2)
    list2=LinkedList(nodeli3)
    zipLists(list1,list2)
    actual=list1.to_string()
    expected="{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> Null"
    assert actual==expected

def test_one_longer1():
    nodel2=Node(3)
    nodel3=Node(1,nodel2)
    list1=LinkedList(nodel3)
    nodeli1=Node(4)
    nodeli2=Node(9,nodeli1)
    nodeli3=Node(5,nodeli2)
    list2=LinkedList(nodeli3)
    zipLists(list1,list2)
    actual=list1.to_string()
    expected="{1} -> {5} -> {3} -> {9} -> {4} -> Null"
    assert actual==expected

def test_one_longer2():
    nodel1=Node(2)
    nodel2=Node(3,nodel1)
    nodel3=Node(1,nodel2)
    list1=LinkedList(nodel3)
    nodeli2=Node(9)
    nodeli3=Node(5,nodeli2)
    list2=LinkedList(nodeli3)
    zipLists(list1,list2)
    actual=list1.to_string()
    expected="{1} -> {5} -> {3} -> {9} -> {2} -> Null"
    assert actual==expected