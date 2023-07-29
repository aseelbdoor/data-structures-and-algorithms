# Tree Intersection
Write a function called tree_intersection that takes two binary trees as parameters. Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process
![img](./tree%20intersection.png)

## Approach & Efficiency
.. Time : O(n) / Space : O(n)
- This function takes two binary trees, 'tr1' and 'tr2', as input.
- It creates a hash table to store the unique values encountered while traversing the binary trees.
- Then, it performs a depth-first traversal of both trees simultaneously and adds each unique value
        encountered to the hash table. If a value already exists in the hash table, it means the value is common
        to both trees, and it is appended to the 'arr' list.
- Finally, the function returns the list of common values found in both trees. If no common values are found,
        it returns a message indicating that there are no common values.

## Solution
To run the code: `python python/tree_intersection/tree_intersection.py`

[Open the code](./tree_intersection.py)