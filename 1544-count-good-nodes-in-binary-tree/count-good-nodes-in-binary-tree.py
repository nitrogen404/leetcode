# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if not node:
                return 0
            
            good = 0
            if node.val >= max_value:
                good = 1
            
            max_value = max(max_value, node.val)
            left = dfs(node.left, max_value)
            right = dfs(node.right, max_value)
            return good + left + right
        return dfs(root, root.val)