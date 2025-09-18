# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxlen = 0
        def dfs(currentNode, currentLen):
            nonlocal maxlen
            if not currentNode:
                return 
            currentLen += 1
            maxlen = max(currentLen, maxlen)
            dfs(currentNode.left, currentLen)
            dfs(currentNode.right, currentLen)
        dfs(root, 0)
        return maxlen