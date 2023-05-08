# data-structures-and-algorithms
Write a function which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![img]()

## Approach & Efficiency
- Loop throw index of needed list 
- if the element of index == the wanted element return this index
- if the loop ended without index the function will return -1

Time Complexity : **O(n)**

Space Complexity : **O(1), constant**

## Example
[4, 8, 15, 16, 23, 42], 15 ==> 2

[-131, -82, 0, 27, 42, 68, 179], 42 ==> 4

[11, 22, 33, 44, 55, 66, 77], 90 ==> -1

[1, 2, 3, 5, 6, 7], 4 ==> -1

[Click here to open the code](./sequentialSearch.py)