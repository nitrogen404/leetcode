# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        result = []
        while queue:
            currentNode = queue.popleft()
            if currentNode:
                result.append(str(currentNode.val))
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                result.append("null")
        return ",".join(result)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if index < len(nodes) and nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if index < len(nodes) and nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))