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
    - This method takes an input string and finds the first word that occurs more than once in the string.
        The input string is processed by removing leading and trailing whitespaces and converting it to lowercase.
        Then, the string is split into individual words based on spaces.
        The method uses a hash table (array of linked lists) to keep track of each word and its count.
        The hash function is applied to each word to determine the index in the hash table.
        If the word is not present in the hash table, it is inserted as a new node in the linked list at the corresponding index.
        If the word is already present, its count is incremented in the linked list.
        The method keeps track of the first word that occurs more than once and its repetition count.
        Finally, the method returns a formatted string with the first repeated word and its repetition count.

## Whiteboard
- repeated_word
![repeate](./Repeated%20Word.png)

## How to run the code 
`python3 python/hashtable/hashtable.py`

## Test
`pytest`

**repeated_word Tests**

|Input|Output|
|:--------|:--------|
|"Once upon a time, there was a brave princess who..."|"The first word to occur more than once in this string is (a) that repeated : 2 times"|
|"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."|"The first word to occur more than once in this string is (it) that repeated : 10 times"|
|"It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."|"The first word to occur more than once in this string is (summer) that repeated : 2 times"|
|""|"There is no words in this string"|

[Open the code](./hashtable.py)
