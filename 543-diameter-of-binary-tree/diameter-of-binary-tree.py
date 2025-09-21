# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(currentNode, currentHeight):
            nonlocal maxDiameter
            if currentNode is None:
                return 0
            leftheight = dfs(currentNode.left, currentHeight + 1)
            rightHeight = dfs(currentNode.right, currentHeight + 1)
            maxDiameter = max(maxDiameter, leftheight + rightHeight)
            return 1 + max(leftheight, rightHeight)
        
        dfs(root, 0) 
        return maxDiameter