# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in arrA:
        for j in arrB:
            if i > j:
                merged_arr = [j,i]
            else:
                merged_arr = [i,j]

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        arrA = arr[:(len(arr)/2)]
        arrB = arr[(len(arr)/2):]
        if len(arrA) > 1 or len(arrB) > 1:
            merge_sort(arrA)
            merge_sort(arrB)
    else:
        arr = merge(arrA, arrB)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
