from python.sorting.insertion.insertion_sort import Sort


def test_Reverse_sorted():
    sort_instance = Sort()
    input_list = [20,18,12,8,5,-2]
    actual = sort_instance.insertion_sort(input_list)
    expected=[-2,5,8,12,18,20]
    assert actual==expected

def test_Few_uniques():
    sort_instance = Sort()
    input_list = [5,12,7,5,5,7]
    actual = sort_instance.insertion_sort(input_list)
    expected=[5,5,5,7,7,12]
    assert actual==expected

def test_Nearly_sorted():
    sort_instance = Sort()
    input_list = [2,3,5,7,13,11]
    actual = sort_instance.insertion_sort(input_list)
    expected=[2,3,5,7,11,13]
    assert actual==expected