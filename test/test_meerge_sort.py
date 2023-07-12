from python.sorting.merge.merge_sort import merge,mergeSort

def test_Reverse_sorted():
    input_list = [20,18,12,8,5,-2]
    mergeSort(input_list)
    actual = input_list
    expected=[-2,5,8,12,18,20]
    assert actual==expected

def test_Few_uniques():
    input_list = [5,12,7,5,5,7]
    mergeSort(input_list)
    actual = input_list
    expected=[5,5,5,7,7,12]
    assert actual==expected

def test_Nearly_sorted():
    input_list = [2,3,5,7,13,11]
    mergeSort(input_list)
    actual = input_list
    expected=[2,3,5,7,11,13]
    assert actual==expected