# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)) : 
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index] 

    return arr

import random

A = [1, 45, 23, 33, 5, 23, 34, 22, 11, 0, 5]
print ("Selection sort")
print(selection_sort(A))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr