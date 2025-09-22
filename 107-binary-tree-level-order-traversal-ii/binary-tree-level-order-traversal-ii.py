# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for _ in range(levelSize):
                node = queue.popleft()
                levelNodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levelNodes)
        result.reverse()
        return result 