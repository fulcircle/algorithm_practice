from random import randint

# For reference
# CHILD_NODES = 2
# NUM_NODES = 24

class Node:

    def __init__(self, value, visited=0):
        self.value = value
        self.visited = visited
        self.children = []
        self.data = None

    def add_child(self, child):
        self.children.append(child)


def random_value():
    return randint(0,9)


def generateTree(num_children, total_nodes):
    root = Node(random_value())
    free_nodes = [root]
    num_nodes = 1

    while(num_nodes < total_nodes):
        current_node = free_nodes.pop(0)
        child_nodes = 0

        while(child_nodes < num_children):
            child_node = Node(random_value())
            current_node.add_child(child_node)
            free_nodes.append(child_node)

            child_nodes += 1
            num_nodes += 1

    return root
