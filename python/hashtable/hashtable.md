# Hash Table

## Required for .venv
`pip install pytest`
## Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
## Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
  - Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
  - **insert**
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
## HashTable
  - **set**
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.

  - **get**
    - Arguments: key
    - Returns: Value associated with that key in the table

  - **has**
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
  - **keys**
    - Returns: Collection of keys
  - **hash**
    - Arguments: key
    - Returns: Index in the collection for that key
  - **repeated_word**
    - Arguments: string
    - Returns: first word to occur more than once in a string


## How to run the code 
`python3 python/hashtable/hashtable.py`

## Test
`pytest`

[Open the code](./hashtable.py)
