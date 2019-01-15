my_list = [52,8,45,43,6,56,76,36,54,12,34,98,41,30,-1]

def quicksort_recursive(arr):
    high = []
    low = []
    pivot_list = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)
            else:
                pivot_list.append(i)
        high = quicksort_recursive(high)
        low = quicksort_recursive(low)

    return low + pivot_list + high

print(quicksort_recursive(my_list))