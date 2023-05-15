class Sort:
    def __init__(self) -> None:
        pass

    def insertion_sort(self, lst):
        # Using a for loop, iterate through the list
        for i in range(1, len(lst)):
            # Store the current item to be inserted at the right place
            item = lst[i]
            # Initialize a variable to keep track of the index to insert the current item
            index = 0
            # Using a for loop iterate through items on the left of the current item
            # Iterate the array on reverse because it's easier to shift elements to the right
            for j in range(i - 1, -1, -1):
                # If the current item in the inner array is greater than the current item
                if lst[j] > item:
                    # Shift the item one index to the right to make space for the current item
                    lst[j + 1] = lst[j]
                # else, get the current index in the inner array and break the inner loop
                # because we found the correct index to insert the current item
                else:
                    index = j + 1
                    break
            # insert the item in the correct index in the array
            lst[index] = item

        return lst

    def bubble_sort(self, lst):
        # Using a for loop, iterate through the list
        # An inner array iterates through the list and compares two adjacent items
        # If the left item is greater than right item, swap them
        # By the time the inner loop is complete the largest item in the array should be to the right
        # To avoid redudancy, the end index of the inner array keeps getting smaller as right most items are sorted
        # Repeat until the whole list is sorted

        for i in range(len(lst)):
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp

        return lst
