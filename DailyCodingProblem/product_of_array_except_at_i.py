# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def product_of_array_except_at_i(seq):

    total = 1
    for val in seq:
        total *= val
    
    new_seq = []
    for val in seq:
        new_seq.append(total // val)
    
    return new_seq



def product_of_array_except_at_i_no_division(seq):

    length = len(seq)
    product_from_left = [1]*length
    product_from_right = [1]*length
    new_seq = [0]*length

    current_product = 1
    for idx in range(0, length):
        if idx == 0:
            continue
        else:
            current_product *= seq[idx-1]
            product_from_left[idx] = current_product
    
    current_product = 1
    for idx in range(length-1, -1, -1):
        if idx == length-1:
            continue
        else:
            current_product *= seq[idx+1]
            product_from_right[idx] = current_product


    for idx in range(0, length):
        new_seq[idx] = product_from_left[idx] * product_from_right[idx]

    return new_seq


assert(product_of_array_except_at_i([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
assert(product_of_array_except_at_i_no_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])

assert(product_of_array_except_at_i([3, 2, 1]) == [2, 3, 6])
assert(product_of_array_except_at_i_no_division([3, 2, 1]) == [2, 3, 6])
