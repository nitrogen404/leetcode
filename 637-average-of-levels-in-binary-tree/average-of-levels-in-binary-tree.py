# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from collections import deque 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            levelSum = 0
            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average = levelSum / levelSize
            result.append(average)
        return result

