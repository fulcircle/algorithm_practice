# 10/30/2018

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

# Have a great day!

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):

    queue = [node]
    serialize = []

    while len(queue) > 0:
        current_node = queue.pop()
        if current_node == None:
            serialize.append("")
            continue
        else:
            serialize.append(current_node.val)
        
        if not current_node.left and not current_node.right:
            continue
        queue.insert(0, current_node.left)
        queue.insert(0, current_node.right)

    return ",".join(serialize)

def deserialize(serialized):
    serialized_arr = serialized.split(",")
    # (node, height, x-pos)
    root = Node(serialized_arr[0])
    queue = [(root, 0)]

    while len(queue) > 0:
        current_node, idx = queue.pop()

        left_child_idx = 2*idx + 1
        right_child_idx = 2*idx + 2

        if left_child_idx < len(serialized_arr):
            if serialized[left_child_idx] != "":
                left_node = Node(serialized_arr[left_child_idx])
                current_node.left = left_node
                queue.insert(0, (left_node, left_child_idx))
        else:
            break

        if right_child_idx < len(serialized_arr):
            if serialized[right_child_idx] != "":
                right_node = Node(serialized_arr[right_child_idx])
                current_node.right = right_node
                queue.insert(0, (right_node, right_child_idx))
        else:
            break



    return root
        

        



node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))