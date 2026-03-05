# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            leftheight = dfs(node.left)
            rightheight = dfs(node.right)
            if leftheight == -1:
                return -1
            if rightheight == -1:
                return -1
            if abs(leftheight - rightheight) > 1:
                return -1
            return max(leftheight, rightheight) + 1
        return dfs(root) != -1