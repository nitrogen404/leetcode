# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half 
        second = slow.next
        prev = slow.next = None 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        
