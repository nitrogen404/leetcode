# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        result = None
        def search(node):
            nonlocal result
            if not node or result is not None:
                return 
            search(node.left)
            self.k -= 1
            if self.k == 0:
                result = node.val
                return 
            search(node.right)
        search(root)
        return result