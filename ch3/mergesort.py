def merge_sort(input_list):
    '''
        Merge sorting a list in O(nlogn) time

        Arguments:
            :input_list: the unsorted input list that needs to be sorted
    '''

    if len(input_list) > 1:
        print('Splitting ', input_list)
        # Get the midpoint
        midpoint = len(input_list) // 2

        # Split the lists at the midpoint
        left_list = input_list[:midpoint]
        right_list = input_list[midpoint:]

        # recursively merge sort each side (starting at the left most)
        merge_sort(left_list)
        merge_sort(right_list)

        # Initialize the left list index, the right list index, and the 
        # sorted list index
        i = j = k = 0

        # Traverse and merge the sorted lists
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                input_list[k] = left_list[i]
                i += 1
            else:
                input_list[k] = right_list[j]
                j += 1
            k += 1

        # Assing remaining left list values (if any)
        while i < len(left_list):
            input_list[k] = left_list[i]
            i += 1
            k += 1

        # Assign remaining right list values (if any)
        while j < len(right_list):
            input_list[k] = right_list[j]
            j += 1
            k += 1

        # Print the list that is going to be merged into the other one
        print('Merging', input_list)
        return input_list

print(merge_sort([10, 2000, 2032, 43, 21, 12, 43, 20000, 432, 332, 1, 11]))
