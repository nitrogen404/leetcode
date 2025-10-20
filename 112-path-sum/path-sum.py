# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        
        def dfs(node, Sum):
            if not node:
                return False
            Sum += node.val
            if not node.left and not node.right:
                return Sum == target
            return dfs(node.left, Sum) or dfs(node.right, Sum)
        return dfs(root, 0)

            
        