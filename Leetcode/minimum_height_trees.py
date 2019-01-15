# https://leetcode.com/problems/minimum-height-trees/

# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1 :

# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3

# Output: [1]
# Example 2 :

# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5

# Output: [3, 4]
# Note:

# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# ##### NAIVE SOLUTION Time: O(n**2)
# class Solution:
#     def findMinHeightTrees(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         root_heights = {}
#         for root in range(0, n):
#             if root in root_heights:
#                 continue
#             nodes_to_visit = [(root, 0)]
#             max_height = 0
#             visited = []

#             while len(nodes_to_visit) > 0:
#                 current_node, height = nodes_to_visit.pop()

#                 if height > max_height:
#                     max_height = height

#                 visited.append(current_node)

#                 next_nodes = self.getChildren(current_node, edges, visited)
#                 for node in next_nodes:
#                     nodes_to_visit.insert(0, (node, height+1))

#             root_heights[root] = max_height

#         return self.getMinNodes(root_heights)


#     def getChildren(self, node, edges, visited):

#         children = []
#         for edge in edges:
#             if edge[0] == node and edge[1] not in visited:
#                 children.append(edge[1])
#             elif edge[1] == node and edge[0] not in visited:
#                 children.append(edge[0])

#         return children


#     def getMinNodes(self, root_heights):

#         min_nodes = []

#         for node, height in root_heights.items():
#             if len(min_nodes) == 0 or height < root_heights[min_nodes[0]]:
#                 min_nodes = [node]
#             elif height == root_heights[min_nodes[0]]:
#                 min_nodes.append(node)

#         return sorted(min_nodes)

# Optimal solution Time: O(n)
class Solution:

    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


assert(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1])

assert(Solution().findMinHeightTrees(
    6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4])

assert(Solution().findMinHeightTrees(
    6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]) == [3])

assert(Solution().findMinHeightTrees(1, []) == [0])
