# https://www.geeksforgeeks.org/finding-all-subsets-of-a-given-set-in-java/

def subsets_of_set_bits(input_set):
    list_set = list(input_set)
    num_elements = 2**len(list_set)
    num_bits = len("{0:b}".format(num_elements-1))

    all_subsets = []
    for i in range(0, num_elements):
        binary = "{0:b}".format(i).zfill(num_bits)
        subset = []
        for idx, c in enumerate(binary):
            if c == '1':
                subset.append(list_set[idx])
        all_subsets.append(subset)
    
    return all_subsets


# https://www.youtube.com/watch?v=RnlHPR0lyOE
def subsets_of_set_backtracking(input_set):

    # Backtracking
    def generate_bitstrings(i, B, bitstrings, num_elements):
        if i == num_elements:
            bitstrings.append(B.copy())
        else:
            B[i] = 0
            generate_bitstrings(i+1, B, bitstrings, num_elements)

            B[i] = 1
            generate_bitstrings(i+1, B, bitstrings, num_elements) 

    list_set = list(input_set)
    num_elements = len(list_set)
    bitstrings = []
    all_subsets = []
    B = [0]*num_elements
    generate_bitstrings(0, B, bitstrings, num_elements)

    for bitstring in bitstrings:
        temp = []
        for idx, num in enumerate(bitstring):
            if num == 1:
                temp.append(list_set[idx])
        all_subsets.append(temp)

    return all_subsets

input = set([1, 2, 3, 4])
print(subsets_of_set_backtracking(input))