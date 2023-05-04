# data-structures-and-algorithms
Write a function that removes an element from the middle index and shifts other elements in the array to fill the new gap.

## Whiteboard Process
No Whitebord

## Approach & Efficiency
- Import math to use math.floor() from it to convert float number
- Determine the location for the element in the middle to delete it
- Create empty list
- Loop throw needed list 
- Append all elements to the new list until the element we wanted his location
- The code will skip this element using (countinue) and complete append other element

Time Complexity : **O(n)**

Space Complexity : **O(1), constant**

## Example
[42, 8, 15, 23, 42] ==> [42, 8, 23, 42]

[Click here to open the code](./remove.py)