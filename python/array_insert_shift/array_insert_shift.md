# data-structures-and-algorithms
Write a function that takes an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
![img](./Array%20Insert%20Shift.png)

## Approach & Efficiency
 - Import math to use math.ceil() from it to convert float number
- Determine the location for the new element in the middle
- Create empty list
- Loop throw needed list 
- Append all elements to the new list until the element we wanted his location
- The code will append the new element in this location and then append the element itself 

Time Complexity : **O(n)**

Space Complexity : **O(1), constant**

## Example
[42, 8, 15, 23, 42], 16 ==> [42, 8, 15, 16, 23, 42]

[Click here to open the code](./array_insert_shift.py)