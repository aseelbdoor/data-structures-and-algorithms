# Insertion Sort
 Trace insertion sort algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

**Methods:**
- insert
  - Arguments: sorted_list, value
  - Inserts a value into the correct position in a sorted list.
- insertion_sort
  - Arguments: input_list
  - Sorts the input list using the insertion sort algorithm.

## Whiteboard Process
![insertion](./Insertion%20Sort.png)

## Approach & Efficiency
- The Sort class is defined with two methods: insert and insertion_sort. The class is responsible for performing insertion sort on a list.

- The insert method takes a sorted list and a value as input. It finds the correct position for the value in the sorted list, such that the list remains sorted. The method uses a while loop to iterate backwards through the list, comparing the value with each element. If the value is less than the current element, it moves the element one position to the right. Once the correct position is found, the value is inserted into the list using the insert method of the list object.

- The insertion_sort method takes an input list and performs the insertion sort algorithm to sort the elements in ascending order. It initializes a new list called sorted_list with the first element from the input list. Then, it iterates over the remaining elements in the input list using a for loop. For each element, it calls the insert method, passing the sorted_list and the element to be inserted. This ensures that the element is inserted into the correct position in the sorted_list while maintaining the sorted order. Finally, the method returns the sorted list.

## Solution
To run the code: `python3 python/sorting/insertion/insertion_sort.py`

**Sort**
|Input|Output|
|:-----|:---|
|[20,18,12,8,5,-2]|[-2,5,8,12,18,20]|
|[5,12,7,5,5,7]|[5,5,5,7,7,12]|
|[2,3,5,7,13,11]|[2,3,5,7,11,13]|

[Open the code](./insertion_sort.py)