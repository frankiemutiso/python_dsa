class Sort:
    def __init__(self) -> None:
        pass

    def insertion_sort(self, lst):
        """
        Steps:
        1. Start with the second element of the list (index 1).
        2. Store the current item in a variable called 'item'.
        3. Initialize a variable 'index' to 0.
        4. Iterate over the sorted section of the list (from the current item's position - 1 to the beginning of the list) in reverse order.
            5. Compare each element in the sorted section with the 'item'.
            6. If the element is larger than the 'item', shift it one position to the right.
            7. If the element is smaller or equal to the 'item', set 'index' to the position where the 'item' should be inserted (current element's position + 1) and break the loop.
        8. Set the element at 'index' in the list to the 'item'.
        9. Repeat steps 2-8 for each remaining element in the list.
        10. Return the sorted list.
        """
        
        for i in range(1, len(lst)):
            item = lst[i]
            index = 0
            for j in range(i - 1, -1, -1):
                if lst[j] > item:
                    lst[j + 1] = lst[j]
                else:
                    index = j + 1
                    break
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

    def selection_sort(self, lst):
        """
        1. Begin by initializing a for loop to keep track of the number of steps.
        2. In order to determine the index of the smallest item, assign the current step as the index.
        3. Next, set up an inner loop to compare the items in the list with the smallest item.
        4. If the current item in the inner loop is smaller than the current smallest item, update the index of the smallest item.
        5. Once the inner loop terminates, swap the smallest item with the item at the current iteration in the outer loop.
        6. Repeat these steps until the list is fully sorted.
        """
        for step in range(0, len(lst)):
            smallest_idx = step

            for j in range(step + 1, len(lst)):
                if lst[j] < lst[smallest_idx]:
                    smallest_idx = j

            temp = lst[step]
            lst[step] = lst[smallest_idx]
            lst[smallest_idx] = temp

        return lst

    def quick_sort():
        """
        1. Select a pivot element - preferably last item
        2. Iterate throught the list and check if there is an element smaller than pivot element
        3. For the first element greater than pivot element, get its index
        4. Iterate the array looking for an item smaller than pivot element
        - If found, swap the element with greater element index, if not found swap it with pivot element
        5. Move the greater element index to the next item that is greater than pivot element and repeat step 4
        """
        
        pass
