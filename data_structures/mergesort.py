
my_list = [52,8,45,43,6,56,76,36,54,12,34,98,41,30,-1]

def mergesort_recursive(arr):

    if len(arr) <= 1:
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    left = mergesort_recursive(arr[:half])
    right = mergesort_recursive(arr[half:])

    return merge(left, right)

def merge(left, right):

    merged = []

    left_ptr = 0
    right_ptr = 0

    while left_ptr < len(left) and right_ptr < len(right):

        if left[left_ptr] < right[right_ptr]:
            merged.append(left[left_ptr])
            left_ptr += 1

        elif left[left_ptr] > right[right_ptr]:
            merged.append(right[right_ptr])
            right_ptr += 1

        elif left[left_ptr] == right[right_ptr]:
            merged += [left[left_ptr], right[right_ptr]]
            left_ptr += 1
            right_ptr += 1

    merged += left[left_ptr:]
    merged += right[right_ptr:]
    return merged

print(mergesort_recursive(my_list))