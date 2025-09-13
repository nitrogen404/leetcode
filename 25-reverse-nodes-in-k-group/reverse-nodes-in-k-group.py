# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = getKthNode(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev, current = kth.next, groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next