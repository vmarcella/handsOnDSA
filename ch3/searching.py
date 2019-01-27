'''
    Linear search program to search an element, and then return the index position
    of that element within the array
'''

def searching(arr, item):
    '''
        Find an item within an array and return it's index if found

        Arguments:
            :arr: array to search
            :item: item to search for
    '''
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1
