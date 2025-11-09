# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            trees = []
            if start > end:
                return [None]
            for rootVal in range(start, end + 1):
                leftSubTree = build(start, rootVal - 1)
                rightSubTree = build(rootVal + 1, end)
                for left in leftSubTree:
                    for right in rightSubTree:
                        root = TreeNode(rootVal)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        return build(1, n)