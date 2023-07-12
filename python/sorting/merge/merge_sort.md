# Insertion Sort
 Trace insertion sort algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

**Methods:**
- merge
  - Arguments: left, right, arr
  - Merges two sorted subarrays into a single sorted array.
- mergeSort
  - Arguments: array
  - Sorts an array using the merge sort algorithm.

## Whiteboard Process
![insertion](./merge%20sort.png)

## Approach & Efficiency
- The merge function takes two sorted subarrays, left and right, and merges them into a single sorted array arr. It iterates over the elements of left and right using three indices i, j, and k. Comparisons are made between corresponding elements of left and right, and the smaller element is placed in the correct position in arr. The merging process modifies arr in-place.

- The mergeSort function performs the merge sort algorithm on the input array. It first checks if the array has more than one element. If so, it calculates the midpoint mid of the array and divides it into two halves, left and right. The function recursively calls itself on left and right to sort them separately. Finally, it merges the sorted left and right subarrays using the merge function to obtain the final sorted array.

- The code follows the divide-and-conquer approach of merge sort, where the array is recursively divided into smaller subarrays until they contain only one element, and then these subarrays are merged back together in sorted order.

## Solution
To run the code: `python3 python/sorting/merge/merge_sort.py`

**Sort**
|Input|Output|
|:-----|:---|
|[20,18,12,8,5,-2]|[-2,5,8,12,18,20]|
|[5,12,7,5,5,7]|[5,5,5,7,7,12]|
|[2,3,5,7,13,11]|[2,3,5,7,11,13]|

[Open the code](./merge_sort.py)