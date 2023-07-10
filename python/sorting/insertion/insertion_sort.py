
class Sort:
    """
    A class that provides methods for performing insertion sort on a list.

    Methods:
        insert(sorted_list, value):
            Inserts a value into the correct position in a sorted list.
        
        insertion_sort(input_list):
            Sorts the input list using the insertion sort algorithm.

    """
    def insert(self, sorted_list, value):
        """
        Inserts a value into the correct position in a sorted list.

        Parameters:
            sorted_list (list): A sorted list of values.
            value: The value to be inserted into the sorted list.

        Returns:
            None

        Description:
            This method takes a sorted list and a value as input.
            It finds the correct position for the value in the sorted list, such that the list remains sorted.
            The value is inserted into the correct position using the 'insert' method of the list object.
            The insert operation modifies the 'sorted_list' in-place, and it does not return any value.
        """
        i = len(sorted_list) - 1
        while i >= 0 and value < sorted_list[i]:
            i -= 1
        sorted_list.insert(i + 1, value)

    def insertion_sort(self, input_list):
        """
        Sorts the input list using the insertion sort algorithm.

        Parameters:
            input_list (list): The list to be sorted.

        Returns:
            list: The sorted list.

        Description:
            This method takes an input list and performs the insertion sort algorithm to sort the elements in ascending order.
            It initializes a 'sorted_list' with the first element from the input list.
            Then, it iterates over the remaining elements in the input list, and for each element, it calls the 'insert' method
            to insert it into the correct position in the 'sorted_list'.
            The method returns the final sorted list.
        """
        sorted_list = [input_list[0]]
        for i in range(1, len(input_list)):
            self.insert(sorted_list, input_list[i])
        return sorted_list

#main
if __name__=="__main__":
    sort_instance = Sort()
    input_list = [8,4,23,42,16,15]
    sorted_list = sort_instance.insertion_sort(input_list)
    print(sorted_list)