from python.tree_intersection.tree_intersection import tree_intersection
from python.tree.binaryTree import Tnode,binaryTree
import pytest

@pytest.fixture
def tree1():
  tree1 = binaryTree()
  tree1.root= Tnode(150)
  tree1.root.left=Tnode(100)
  tree1.root.right = Tnode(250)
  tree1.root.left.left = Tnode(75)
  tree1.root.left.right = Tnode(160)
  tree1.root.left.right.left = Tnode(125)
  tree1.root.left.right.right = Tnode(175)
  tree1.root.right.left = Tnode(200)
  tree1.root.right.right = Tnode(350)
  tree1.root.right.right.left = Tnode(300)
  tree1.root.right.right.left = Tnode(500)
  return tree1


@pytest.fixture
def tree2():
  tree2 = binaryTree()
  tree2.root= Tnode(42)
  tree2.root.left=Tnode(100)
  tree2.root.right = Tnode(600)
  tree2.root.left.left = Tnode(15)
  tree2.root.left.right = Tnode(160)
  tree2.root.left.right.left = Tnode(125)
  tree2.root.left.right.right = Tnode(175)
  tree2.root.right.left = Tnode(200)
  tree2.root.right.right = Tnode(350)
  tree2.root.right.right.left = Tnode(4)
  tree2.root.right.right.left = Tnode(500)
  return tree2


@pytest.fixture
def tree3():
  tree3 = binaryTree()
  return tree3

@pytest.fixture
def tree4():
  tree4 = binaryTree()
  tree4.root= Tnode(50)
  tree4.root.left=Tnode(70)
  tree4.root.right = Tnode(250)
  tree4.root.left.left = Tnode(14)
  tree4.root.left.right = Tnode(30)
  return tree4

def test_found(tree1,tree2):
  actual=tree_intersection(tree1,tree2)
  expected=[100, 160, 125, 175, 200, 350, 500]
  assert actual == expected

def test_not_found(tree2,tree4):
  actual=tree_intersection(tree4,tree2)
  expected="There is no values found in both trees"
  assert actual == expected

def test_empty(tree1,tree3):
  with pytest.raises(Exception):
    tree_intersection(tree1,tree3)