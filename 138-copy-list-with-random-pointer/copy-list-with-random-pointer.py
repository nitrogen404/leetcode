"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        current = head
        copies = {}
        
        while current:
            copies[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copy_node = copies[current]
            if current.next:
                copy_node.next = copies[current.next]
            if current.random:
                copy_node.random = copies[current.random]
            current = current.next
        return copies[head]