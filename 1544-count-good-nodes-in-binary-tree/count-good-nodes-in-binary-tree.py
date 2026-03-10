# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, maxSofar):
            nonlocal good
            if not node:
                return 
            if node.val >= maxSofar:
                good += 1
            newMax = max(maxSofar, node.val)
            dfs(node.left, newMax)
            dfs(node.right, newMax)
        dfs(root, root.val)
        return good