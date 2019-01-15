# binary_search_recursive
# binary_search_iterative
# quicksort_recursive
# mergesort_recursive
# bfs
# dfs
# dfs_recursive
# Max heap

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


def quicksort_recursive(arr):

    if len(arr) <= 1:
        return arr

    high = []
    low = []
    pivots = []

    pivot = arr[0]

    for val in arr:
        if val > pivot:
            high.append(val)
        elif val < pivot:
            low.append(val)
        else:
            pivots.append(val)

    return quicksort_recursive(low) + pivots + quicksort_recursive(high)


def mergesort_recursive(arr):

    if len(arr) <= 1:
        return arr

    def merge(left, right):

        left_ptr = 0
        right_ptr = 0

        merged = []

        while left_ptr < len(left) and right_ptr < len(right):

            if left[left_ptr] < right[right_ptr]:
                merged.append(left[left_ptr])
                left_ptr += 1
            elif right[right_ptr] < left[left_ptr]:
                merged.append(right[right_ptr])
                right_ptr += 1
            else:
                merged.append(left[left_ptr])
                merged.append(right[right_ptr])
                left_ptr += 1
                right_ptr += 1
            
        merged.extend(left[left_ptr:])
        merged.extend(right[right_ptr:])

        return merged

        
    middle = len(arr) // 2
    left = mergesort_recursive(arr[0:middle])
    right = mergesort_recursive(arr[middle:])
    return merge(left, right)
                

def bfs(root, key):

    node_queue = [root]

    while len(node_queue) > 0:

        current_node = node_queue.pop(0)
        if current_node.val == key:
            return current_node
        else: 
            node_queue.extend(current_node.children)

    return None

def dfs(root, key):

    node_stack = [root]

    while len(node_stack) > 0:

        current_node = node_stack.pop()

        if current_node.val == key:
            return current_node
        else:
            node_stack.append(current_node.children)
    

def dfs_recursive(root, key):

    if root.val == key:
        return root
    else:
        for child in root.children:
            return dfs_recursive(child, key)
    
    return None


class MaxHeap:

    def __init__(self, arr):
        self.arr = arr
        self.build_heap()

    def build_heap(self):

        for i in range(len(self.arr) // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2

        largest = i
        if l < len(self.arr) and self.arr[l] > self.arr[largest]:
            largest = l

        if r < len(self.arr) and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.max_heapify(largest)

    def push(self, val):
        self.arr.append(val)
        self.build_heap()

    def pop(self):
        if len(self.arr) > 0:
            val = self.arr.pop(0)

            if len(self.arr) > 0:
                last_item = self.arr.pop()
                self.arr.insert(0, last_item)
                self.build_heap()

            return val

        return None



arr = [1, 2, 3, 4, 5]
# print(binary_search_recursive(arr, 0, len(arr)-1, 3)) # 2
# print(binary_search_recursive(arr, 0, len(arr)-1, 1)) # 0
# print(binary_search_recursive(arr, 0, len(arr)-1, 5)) # 4

# print(binary_search_iterative(arr, 3)) # 2
# print(binary_search_iterative(arr, 1)) # 0
# print(binary_search_iterative(arr, 5)) # 4

sort_array_1 = [4, 34, 5, 56, 34]
sort_array_2 = []
sort_array_3 = [1, 2, 3, 4, 5]
sort_array_4 = [5, 4, 3, 2, 1]
# print(quicksort_recursive(sort_array_1)) # [4, 5, 34, 34, 56]
# print(quicksort_recursive(sort_array_2)) # []
# print(quicksort_recursive(sort_array_3)) # [1, 2, 3, 4, 5]
# print(quicksort_recursive(sort_array_4)) # [1, 2, 3, 4, 5]

# print(mergesort_recursive(sort_array_1))  # [4, 5, 34, 34, 56]
# print(mergesort_recursive(sort_array_2))  # []
# print(mergesort_recursive(sort_array_3))  # [1, 2, 3, 4, 5]
# print(mergesort_recursive(sort_array_4))  # [1, 2, 3, 4, 5]


arr = [1, 2, 3, 4, 5, 6, 7, 8]
# m = MaxHeap(arr)
# m.pop()
# m.pop()
# m.push(8)
# print(m.arr) # [8, 5, 6, 4, 1, 2, 3]
