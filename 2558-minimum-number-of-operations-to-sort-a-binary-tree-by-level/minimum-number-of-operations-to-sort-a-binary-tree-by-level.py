# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        operations = 0
        while queue:
            width = len(queue)
            level = []
            for i in range(width):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            operations += self.minswaps(level)
        return operations
    
    def minswaps(self, level):
        levelSort = sorted(level)
        rank = {val: i for i, val in enumerate(levelSort)}
        position = [rank[x] for x in level]
        visited = [False] * len(level)
        swaps = 0

        for i in range(len(level)):
            if visited[i] or position[i] == i:
                continue
            cycleLen = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = position[j]
                cycleLen += 1
            swaps += cycleLen - 1
        return swaps

