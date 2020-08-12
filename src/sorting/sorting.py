# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a_idx = 0
    b_idx = 0

    for i in range(len(merged_arr)):
        if b_idx > len(arrB) - 1:
            merged_arr[i] = arrA[a_idx]
            a_idx += 1

        elif a_idx > len(arrA) - 1:
            merged_arr[i] = arrB[b_idx]
            b_idx += 1

        else:
            if arrA[a_idx] < arrB[b_idx]:
                merged_arr[i] = arrA[a_idx]
                a_idx += 1

            else:
                merged_arr[i] = arrB[b_idx]
                b_idx += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    middle = len(arr) // 2
    LH = arr[:middle]
    RH = arr[middle:]

    if len(LH) > 1:
        LH = merge_sort(LH)

    if len(RH) > 1:
        RH = merge_sort(RH)

    arr = merge(LH, RH)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
