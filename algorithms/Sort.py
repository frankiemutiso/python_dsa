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
        """
        1. Use two loops to iterate through the list
        - The outer loop determines the number of iterations
        - The number of iterations in the inner loop reduce as the number of iterations in the outer loop increase
        - The iterations on the inner loop reduce because the assumption is that right most items are sorted
        2. An if condition in the inner loop compares two adjacent items
        3. If the item on the left is greater than item on the right, swap the items
        4. Repeat until the whole list is sorted
        """

        for i in range(len(lst)):
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp

        return lst
