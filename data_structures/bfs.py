import vik_tree

def bfsTraverseTree(tree):
    node_queue = [tree]

    while len(node_queue) > 0:
       node = node_queue.pop(0) 
       print(node.value)
       node_queue.extend(node.children)

tree = vik_tree.generateTree()
bfsTraverseTree(tree)