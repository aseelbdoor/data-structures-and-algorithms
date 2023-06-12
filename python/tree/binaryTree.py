# from assest import Queue
from python.tree.assest import Queue


class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None

class binaryTree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    if not self.root:
      return self.root
    output = []
    queue = Queue()
    queue.enqueue(self.root)
    while not queue.is_empty():
      front = queue.dequeue()
      output.append(front.value)
      if front.left :
          queue.enqueue(front.left)
      if front.right :
          queue.enqueue(front.right)  
    return output

  def pre_order(self):
    arr=[]
    def _walk(root):
      arr.append(root.value)
      if root.left :
        _walk(root.left)
      if root.right :
        _walk(root.right)
    _walk(self.root)
    return arr

  def in_order(self):
    arr=[]
    def _walk(root):
      if root.left :
        _walk(root.left)
      arr.append(root.value)

      if root.right :
        _walk(root.right)
    _walk(self.root)
    return arr
  
  def post_order(self):
    arr=[]
    def _walk(root):
      if root.left :
        _walk(root.left)
      if root.right :
        _walk(root.right)
      arr.append(root.value)
    _walk(self.root)
    return arr
  
  def maximum(self):
    if self.root is None:
        return
    value=[self.root.value]
    def _walk(root):
        if root.value>value[0]:
          value[0]=root.value
        if root.left :
          _walk(root.left)
        if root.right :
          _walk(root.right)
    _walk(self.root)
    return value[0]
    


class  binarySearch_tree(binaryTree):
    def __init__(self):
      super().__init__()

    def add(self,value):
      if self.root is None:
        self.root = Tnode(value)
        return
      def _walk(root,value):
        if root.value> value:
          if root.left :
            _walk(root.left,value)
          else:
            root.left=Tnode(value)
        if root.value<=value:
          if root.right :
            _walk(root.right,value)
          else:
            root.right=Tnode(value)
      _walk(self.root,value)

    def contains(self,value):
      def _walk(root,value):
        if root is None:
          return False
        if root.value== value:
          return True
        if root.value> value:
          return _walk(root.left,value)
        if root.value<value:
          return _walk(root.right,value)
      return _walk(self.root,value)

if __name__ == "__main__":
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
  print(tree.pre_order() )
  print("###############")
  print(tree.maximam())
  # tree.add(55)
  # tree.add(60)
  # tree.add(60)
  # print(tree.pre_order() )
  # print(tree.contains(60))