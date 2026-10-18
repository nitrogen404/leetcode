# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count, answer = 0, 0
        def inorder(node):
            nonlocal count, answer
            if not node:
                return 
            
            inorder(node.left)
            count += 1
            if count == k:
                answer = node.val
                return 
            
            inorder(node.right)
        
        inorder(root)
        return answer
