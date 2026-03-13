# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        HEIGHT = self.height(root)
        rows = HEIGHT + 1
        cols = 2 ** (HEIGHT + 1) - 1
        res = [[""] * cols for _ in range(rows)]

        queue = deque([(root, 0, (cols - 1) // 2)])
        
        while queue:
            node, r, c = queue.popleft()
            res[r][c] = str(node.val)
            offset = 2 ** (HEIGHT - r - 1)
            
            if node.left:
                queue.append((node.left, r + 1, c - offset))
            if node.right:
                queue.append((node.right, r + 1, c + offset))

        return res


    def height(self, node):
        if not node:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)
    