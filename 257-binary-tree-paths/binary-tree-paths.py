# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if not root:
            return []
        
        def dfs(node, path):
            nonlocal result
            if not node:
                return 
            if not node.left and not node.right:
                result.append(path)
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
        dfs(root, str(root.val))
        return result