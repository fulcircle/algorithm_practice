# Problem: Find the left-most node at each level of a binary tree

# BFS Solution
import vik_tree

def left_most_node_iterative(root):

    root.data = {"level": 0}
    data = [root]
    highest_level = 0

    node_queue = [root]
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)
        for child in current_node.children:
            child.data = {"level": current_node.data["level"] + 1}

        if current_node.data["level"] > highest_level:
            highest_level += 1
            data.append(current_node)

        node_queue.extend(current_node.children)

    return data

tree = vik_tree.generateTree(2, 24)
result = left_most_node_iterative(tree)

print_r = [[node.data["level"], node.value] for node in result]
print(print_r)
