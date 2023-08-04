# Hashmap Left Join
Write a function called left join have two hash maps as arguments. The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values. You should return The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard Process
![img](left%20join.png)

## Approach & Efficiency
.. Time : O(n*m) / Space : O(n+m)
- It takes two hash tables, ht1 and ht2, as input.

- It retrieves the keys from both ht1 and ht2 and stores them in the keys1 and keys2 lists, respectively.

- It initializes an empty list called baselist, which will hold the results of the left join operation.

- The function then iterates through each key in keys1 using a loop:

  - a. For each key i, it creates a new list new and appends the key to it.

  - b. It retrieves the value associated with the key i in ht1 using the ht1.get(i) method and appends it to the new list.

  - c. It checks if the key i is present in keys2 (i.e., if it exists in both hash tables).

  - d. If the key i is found in keys2, it retrieves the corresponding value from ht2 using the ht2.get(i) method and appends it to the new list.

  - e. If the key i is not found in keys2, it appends the string 'Null' to the new list.

  - f. The new list, containing the key and values from ht1 and ht2 (if available), is then appended to the baselist.

- Once all keys in keys1 have been processed, the function returns the baselist, which represents the result of the left join operation.

## Solution
To run the code: `python python/hashmap_left_join/hashmap_left_join.py`

[Open the code](./hashmap_left_join.py)