# Challenge Title
**Node**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree**

Create a Binary Tree class
Define a method for each of the depth first traversals:
- pre order
- in order
- post order

find maximum value
- Arguments: none
- Returns: number

Each depth first traversal method should return an array of values, ordered appropriately.

**Binary Search Tree** 

Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
- Add
  - Arguments: value
  - Return: nothing
  - Adds a new node with that value in the correct location in the binary search tree.
- Contains
  - Argument: value
  - Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process
![max](./C.png)

## Approach & Efficiency
**pre order**  .. Time : O(n) / Space : O(n)
- Initialize an empty array arr to store the traversal result.
- Define an inner function _walk that takes a root parameter representing the current node being visited.
- Inside _walk, append the value of the current node (root.value) to the arr.
- Check if the current node has a left child (root.left). If it does, recursively call _walk on the left child to visit it and its subtree.
- Check if the current node has a right child (root.right). If it does, recursively call _walk on the right child to visit it and its subtree.
- Call _walk on the root of the binary tree (self.root).
- Return the arr containing the values in the pre-order traversal order.

**in order**  .. Time : O(n) / Space : O(n)

- Initialize an empty array arr to store the traversal result.
- Define an inner function _walk that takes a root parameter representing the current node being visited.
- Check if the current node has a left child (root.left). If it does, recursively call _walk on the left child to visit it and its subtree.
- Append the value of the current node (root.value) to the arr.
- Check if the current node has a right child (root.right). If it does, recursively call _walk on the right child to visit it and its subtree.
- Call _walk on the root of the binary tree (self.root).
- Return the arr containing the values in the in-order traversal order.

**post order**  .. Time : O(n) / Space : O(n)

- Initialize an empty array arr to store the traversal result.
- Define an inner function _walk that takes a root parameter representing the current node being visited.
- Check if the current node has a left child (root.left). If it does, recursively call _walk on the left child to visit it and its subtree.
- Check if the current node has a right child (root.right). If it does, recursively call _walk on the right child to visit it and its subtree.
- Append the value of the current node (root.value) to the arr.
- Call _walk on the root of the binary tree (self.root).
- Return the arr containing the values in the post-order traversal order.

**Add**  .. Time : O(log n) / Space : O(1)

- Check if the root of the binary search tree is None. If it is, that means the tree is empty, so we create a new node with the given value and set it as the root of the tree. Then we return, as the insertion is complete.
- Define an inner function _walk that takes two parameters: root representing the current node being visited, and value representing the value to be inserted.
- Compare the value with the value of the current node (root.value) to determine the correct location for insertion.
  - If the value is less than the current node's value (root.value), move to the left subtree.
    - If the left child of the current node exists (root.left), recursively call _walk on the left child to continue traversing the left subtree.
    - If the left child of the current node doesn't exist, create a new node with the given value and set it as the left child of the current node.
  - If the value is greater than or equal to the current node's value, move to the right subtree.
    - If the right child of the current node exists (root.right), recursively call _walk on the right child to continue traversing the right subtree.
    - If the right child of the current node doesn't exist, create a new node with the given value and set it as the right child of the current node.
- Call _walk on the root of the binary search tree 

**Contains**  .. Time : O(log n) / Space : O(1)

- Define an inner function _walk that takes two parameters: root representing the current node being visited, and value representing the value to be searched.
- Check if the current node (root) is None. If it is, that means we have reached a leaf node without finding the value. In this case, return False to indicate that the value is not present in the tree.
- Compare the value of the current node (root.value) with the given value to determine the next step:
  - If the value of the current node is equal to the given value, return True to indicate that the value is found in the tree.
  - If the value of the current node is greater than the given value, move to the left subtree.
    - Recursively call _walk on the left child of the current node (root.left) to continue searching for the value in the left subtree.
  - If the value of the current node is less than the given value, move to the right subtree.
    - Recursively call _walk on the right child of the current node (root.right) to continue searching for the value in the right subtree.
- Call _walk on the root of the binary search tree (self.root) and the given value to start the search process.
- Return the result of the _walk function, which will be either True if the value is found or False if it is not found.

**Maximum** .. Time : O(n) / Space : O(1)

- First, the method checks if the root of the binary tree (self.root) is None. If it is, indicating an empty tree, the method returns None.

- If the root is not None, a list named value is initialized with the root value. This list is used to store the maximum value during the traversal.

- The method defines an inner function named _walk that performs the recursive traversal of the tree to find the maximum value.

- Inside the _walk function, the current node's value is compared with the value stored in the value list. If the current node's value is greater than the value in the list, it is updated as the new maximum value.

- The _walk function then recursively calls itself on the left child of the current node (root.left) and the right child of the current node (root.right) if they exist.

- The traversal continues until all nodes have been visited.

- Finally, after the traversal is completed, the method returns the maximum value stored in the value list, which represents the maximum value in the binary tree.

## Solution
To run the code: `python3 python/tree/binaryTree.py`

[Open the code](./binaryTree.py)