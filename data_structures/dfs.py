
import vik_tree

def dfsTraverseTree(tree):
    node_stack = [tree]

    while len(node_stack) > 0:
       node = node_stack.pop() 
       print(node.value)
       node_stack.extend(node.children)

def dfsRecursiveTraverseTree(tree):
    for child in tree.children:
        dfsRecursiveTraverseTree(child)
    print(tree.value)


tree = vik_tree.generateTree()
dfsTraverseTree(tree)
print("=============")
dfsRecursiveTraverseTree(tree)