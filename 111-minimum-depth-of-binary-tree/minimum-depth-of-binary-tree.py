# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        minlen = float('inf')
        def dfs(currentNode, currentLen):
            nonlocal minlen
            if not currentNode:
                return 
            if not currentNode.left and not currentNode.right:
                minlen = min(minlen, currentLen)
                return 
            dfs(currentNode.left, currentLen + 1)
            dfs(currentNode.right, currentLen + 1)
        dfs(root, 1)
        return minlen