# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kthfromStart = head
        for i in range(k - 1):
            kthfromStart = kthfromStart.next
        fast = kthfromStart
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        kthfromStart.val, slow.val = slow.val, kthfromStart.val
        return head