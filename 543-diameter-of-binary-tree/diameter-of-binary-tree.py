# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(currentNode):
            nonlocal maxDiameter
            if currentNode is None:
                return 0
            leftHeight = dfs(currentNode.left)
            rightHeight = dfs(currentNode.right)
            maxDiameter = max(maxDiameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return maxDiameter