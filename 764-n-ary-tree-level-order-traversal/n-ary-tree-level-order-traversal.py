"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                node = queue.popleft()
                currentLevel.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(currentLevel)
        return result