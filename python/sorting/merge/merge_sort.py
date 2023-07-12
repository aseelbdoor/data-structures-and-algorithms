
def merge(left, right, arr):
    """
    Merges two sorted subarrays into a single sorted array.

    Parameters:
        left (list): The left subarray.
        right (list): The right subarray.
        arr (list): The array to merge the subarrays into.

    Returns:
        None

    Description:
        This function takes two sorted subarrays, 'left' and 'right', and merges them into a single sorted array 'arr'.
        It compares the elements of 'left' and 'right' one by one and places them in the correct order in 'arr'.
        The merging process modifies 'arr' in-place, and it does not return any value.
    """
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(array):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
        array (list): The array to be sorted.

    Returns:
        None

    Description:
        This function takes an unsorted array and performs the merge sort algorithm to sort the elements in ascending order.
        It recursively divides the array into two halves until each subarray has only one element.
        Then, it merges the sorted subarrays back together using the 'merge' function to obtain the final sorted array.
        The sorting is performed in-place, and it does not return any value.
    """
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]
        # sort the left side
        mergeSort(left)
        # sort the right side
        mergeSort(right)
        # merge the sorted left and right sides together
        merge(left, right, array)


if __name__=="__main__":
    li=[8,4,23,42,16,15]
    mergeSort(li)
    print(li)