# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# preorder = root, left, right
# inorder = left, root, right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {value: i for i, value in enumerate(inorder)}
        preorderIndex = 0

        def build(left, right):
            nonlocal preorderIndex, hashmap
            if left > right:
                return None
            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)
            preorderIndex += 1
            inOrderIndex = hashmap[rootValue]
            root.left = build(left, inOrderIndex - 1)
            root.right = build(inOrderIndex + 1, right)
            return root
        return build(0, len(inorder) - 1)
