# data-structures-and-algorithms
Write a function which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

**Navigater: Bayan Banat**,
**Driver: Aseel Bdoor**

## Whiteboard Process
![img](./Binary%20Search.png)

## Approach & Efficiency
- import math to use math.floor() from it to convert float number
- Determine the location for the low variable(start index in every part in search) and high variable(last index in every part in search)
- loop while the low is < or = the high (because we change the value of both and need to stoop when there are no remaining parts of the array, this happens when the beginning becomes larger than the end)
- Determine mid (the element in the middle of the array) because the array is ​​sorted in ascending order, we will compare the numbers and choose the part we want and move to it
- if the element in mid position = the wanted element the function will return mid
- if the wanted element is smaller than the element in a mid position that means the wanted position in the left side and the function updates the high to be smaller than the mid to define the end of the left side
- if the wanted element is bigger than the element in a mid position that means the wanted position on the right side and the function updates the low to be bigger than the mid to define the start of the right side
- the loop will still in this way until finding the position for the wanted element
- if the low becomes> high this means the search in all parts of the array is finished, the code will go to else and return -1 if the element does not exist in the array

Time Complexity : **O(log n)**

Space Complexity : **O(1), constant**

## Example
[4, 8, 15, 16, 23, 42], 15 ==> 2

[-131, -82, 0, 27, 42, 68, 179], 42 ==> 4

[11, 22, 33, 44, 55, 66, 77], 90 ==> -1

[1, 2, 3, 5, 6, 7], 4 ==> -1

[Click here to open the code](./binarySearch.py)