# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        memory = {}
        def traverse(node):
            nonlocal memory
            if not node:
                return 
            if node.val not in memory:
                memory[node.val] = 1
            else:
                memory[node.val] += 1
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        if not memory: return []
        
        maxFreq = max(memory.values())
        return [val for val, count in memory.items() if count == maxFreq]
        