# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        maxLength = float('-inf')
        def dfs(node):
            nonlocal maxLength
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            leftPath = rightPath = 0
            if node.left and node.left.val == node.val:
                leftPath = 1 + left
            if node.right and node.right.val == node.val:
                rightPath = 1 + right
            maxLength = max(maxLength, leftPath + rightPath)
            return max(leftPath, rightPath)
        dfs(root)
        return maxLength