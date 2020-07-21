def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i, j, k = 0, 0, 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1

        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1

    return merged_arr


def merge_sort(arr):

    if len(arr) > 1:
        mid = int(len(arr) / 2)
        left = arr[:mid]
        right = arr[mid:]

        left_half = merge_sort(left)
        right_half = merge_sort(right)

        arr = merge(left_half, right_half)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
