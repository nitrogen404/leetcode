# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = None
        def search(node):
            nonlocal result, count
            if not node or result is not None:
                return 
            search(node.left)
            count -= 1
            if count == 0:
                result = node.val
                return 
            search(node.right)
        
        search(root)
        return result
            