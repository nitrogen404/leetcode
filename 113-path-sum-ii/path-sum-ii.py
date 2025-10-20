# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        def dfs(node, Sum, currentList):
            nonlocal result
            if not node:
                return 

            Sum += node.val
            currentList.append(node.val)
            if not node.left and not node.right and Sum == targetSum:
                result.append(list(currentList))
            
            dfs(node.left, Sum, currentList)
            dfs(node.right, Sum, currentList)
            currentList.pop()
        
        dfs(root, 0, [])
        return result