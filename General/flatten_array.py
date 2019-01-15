def flatten_array(arr):
    """Flatten an array.
       Args:
        param1 (list): A list of values.

       Returns:
        list: A flattened array generated from param1."""

    if not isinstance(arr, list):
        raise TypeError("Input value is not a list")

    stack = [arr]
    flattened = []

    # Depth-first traversal flattening of array
    while len(stack) > 0:
        curr_element = stack.pop()
        # If we have to flatten a subarray, append it to our stack
        if isinstance(curr_element, list):
            for ele in curr_element:
                stack.append(ele)
        # Not an array, so we can push it onto our flattened array
        else:
            flattened.insert(0, curr_element)

    return flattened
