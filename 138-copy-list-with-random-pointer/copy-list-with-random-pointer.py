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
        memory = {}
        current = head
        while current:
            memory[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy = memory[current]
            copy.next = memory.get(current.next)
            copy.random = memory.get(current.random)
            current = current.next
        return memory[head]
