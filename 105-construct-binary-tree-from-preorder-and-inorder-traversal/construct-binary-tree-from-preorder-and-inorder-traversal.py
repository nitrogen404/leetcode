# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_index = {}
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i
        
        preorder_index = 0
        
        def dfs(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            rootvalue = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(rootvalue)
            mid = inorder_index[rootvalue]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(inorder) - 1)
        