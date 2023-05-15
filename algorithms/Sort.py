class Sort:
    def __init__(self) -> None:
        pass

    def insertion_sort(lst):
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
