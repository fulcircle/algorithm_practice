def binary_search_recursive(arr, left, right, key):

    if left > right:
        return None

    middle = left + (right - left) // 2

    if key > arr[middle]:
        return binary_search_recursive(arr, middle + 1, right, key)
    elif key < arr[middle]:
        return binary_search_recursive(arr, left, middle-1, key)
    else:
        return middle


def binary_search_iterative(arr, key):

    left = 0
    right = len(arr)-1

    while left <= right:
        
        middle = left + (right - left) // 2

        if key > arr[middle]:
            left = left + 1
        elif key < arr[middle]:
            right = right - 1
        else:
            return middle
    
    return None


array = [1, 2, 3, 4, 5, 6, 7]
test_key = 2
print(binary_search_recursive(array, 0, len(array)-1, test_key))
print(binary_search_iterative(array, test_key))