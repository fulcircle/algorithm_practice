# https://leetcode.com/problems/all-paths-from-source-to-target/

# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Note:

# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of nodes inside one path.

class Solution:
    def allPathsSourceTarget(self, graph):

        source = 0
        target = len(graph)-1
        paths = []

        self.dfs_path(target, [], paths, graph, source)
        
        return paths

    def dfs_path(self, target, current_path, paths, graph, current_node):
        current_path.append(current_node)

        if current_node == target:
            paths.append(current_path.copy())

        for child in self.getChildren(graph, current_node):
            self.dfs_path(target, current_path.copy(), paths, graph, child)


    def getChildren(self, graph, node):
        return graph[node]


print(Solution().allPathsSourceTarget([[1,2], [3], [3], []]))