
def merge(left, right, arr):
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
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, array)


if __name__=="__main__":
    li=[8,4,23,42,16,15]
    mergeSort(li)
    print(li)