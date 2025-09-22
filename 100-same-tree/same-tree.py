# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(node):
            array = []
            queue = deque([node])
            while queue:
                currentnode = queue.popleft()
                if currentnode:
                    array.append(currentnode.val)
                    queue.append(currentnode.left)
                    queue.append(currentnode.right)
                else:
                    array.append(None)
            return array
        return bfs(p) == bfs(q)
        