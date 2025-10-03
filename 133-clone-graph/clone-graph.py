"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}
        queue = deque([node])
        clones[node] = Node(node.val, [])
        while queue:
            currentnode = queue.popleft()
            for neighbor in currentnode.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clones[currentnode].neighbors.append(clones[neighbor])
        return clones[node]
