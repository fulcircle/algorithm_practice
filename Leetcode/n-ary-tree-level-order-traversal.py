# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

import unittest

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        root.level = 0
        current_level = 0
        queue = [root]
        level_nodes = []
        all_nodes = []
        while len(queue) > 0:
            node = queue.pop()

            if current_level != node.level:
                current_level = node.level
                all_nodes.append(level_nodes)
                level_nodes = []

            level_nodes.append(node.val)

            for child in node.children:
                child.level = node.level + 1
                queue.insert(0, child)

        all_nodes.append(level_nodes)
        return all_nodes


class TestSolution(unittest.TestCase):

    def test1(self):
        root = Node(1,
                    [Node(3,
                          [Node(5, []), Node(6, [])]
                          ),
                     Node(2, []),
                     Node(4, [])
                     ]
                    )

        print(Solution().levelOrder(root))
        assert Solution().levelOrder(root) == [[1], [3, 2, 4], [5, 6]]


if __name__ == '__main__':
    unittest.main()

