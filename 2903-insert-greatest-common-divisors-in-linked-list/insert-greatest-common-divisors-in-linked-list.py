# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head
        current = head.next
        while current:
            gcd = ListNode(self.Egcd(prev.val, current.val))
            prev.next = gcd
            gcd.next = current
            prev = current
            current = current.next
        return head 
    
    def Egcd(self, a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)