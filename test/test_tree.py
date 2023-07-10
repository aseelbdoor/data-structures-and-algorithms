import pytest
from python.tree.binaryTree import binarySearch_tree,binaryTree,Tnode

def test_empty():
    tree = binarySearch_tree()
    actual=tree.root
    expected=None
    assert actual==expected

def test_inOrder():
    tree = binarySearch_tree()
    tree.root= Tnode(50)
    tree.root.left=Tnode(20)
    tree.root.right = Tnode(53)
    tree.root.left.left = Tnode(11)
    tree.root.left.right = Tnode(22)
    tree.root.right.right = Tnode(60)
    actual=tree.in_order()
    expected=[11,20,22,50,53,60]
    assert actual==expected

def test_preOrder():
    tree = binarySearch_tree()
    tree.root= Tnode(50)
    tree.root.left=Tnode(20)
    tree.root.right = Tnode(53)
    tree.root.left.left = Tnode(11)
    tree.root.left.right = Tnode(22)
    tree.root.right.right = Tnode(60)
    actual=tree.pre_order()
    expected=[50,20,11,22,53,60]
    assert actual==expected

def test_postOrder():
    tree = binarySearch_tree()
    tree.root= Tnode(50)
    tree.root.left=Tnode(20)
    tree.root.right = Tnode(53)
    tree.root.left.left = Tnode(11)
    tree.root.left.right = Tnode(22)
    tree.root.right.right = Tnode(60)
    actual=tree.post_order()
    expected=[11,22,20,60,53,50]
    assert actual==expected

def test_singleNode():
    tree = binarySearch_tree()
    tree.root=Tnode(10)
    actual=tree.in_order()
    expected=[10]
    assert actual == expected

def test_add():
    tree = binarySearch_tree()
    tree.root=Tnode(10)
    tree.add(5) #left side
    tree.add(30) #right side
    actual=tree.in_order()
    expected=[5,10,30]
    assert actual == expected

def test_contain():
    tree = binarySearch_tree()
    tree.root= Tnode(50)
    tree.root.left=Tnode(20)
    tree.root.right = Tnode(53)
    tree.root.left.left = Tnode(11)
    tree.root.left.right = Tnode(22)
    tree.root.right.right = Tnode(60)
    assert tree.contains(60) and tree.contains(22)

def test_maximam():
   tree = binarySearch_tree()
   tree.root= Tnode(2)
   tree.root.left=Tnode(7)
   tree.root.right = Tnode(5)
   tree.root.left.left = Tnode(2)
   tree.root.left.right = Tnode(6)
   tree.root.left.right.left = Tnode(5)
   tree.root.left.right.right = Tnode(11)
   tree.root.right.right = Tnode(9)
   tree.root.right.right.left = Tnode(4)
   actual=tree.maximum()
   expected=11
   assert actual==expected