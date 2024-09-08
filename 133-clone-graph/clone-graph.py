"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        origin_to_copy = {}
        copy = Node(node.val, None)
        origin_to_copy[node] = copy

        def dfs(origin):
            for neighbor in origin.neighbors:
                if neighbor not in origin_to_copy:
                    copy = Node(neighbor.val, [])
                    origin_to_copy[neighbor] = copy
                    dfs(neighbor)
                origin_to_copy[origin].neighbors.append(origin_to_copy[neighbor])	
        dfs(node)
        return origin_to_copy[node]
	
