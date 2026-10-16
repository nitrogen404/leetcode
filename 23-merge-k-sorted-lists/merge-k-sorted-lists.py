# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        flat_array = []
        for head in lists:
            current = head
            while current:
                flat_array.append(current.val)
                current = current.next
                
            
        if not flat_array:
            return None

        flat_array.sort()

        dummy_node = ListNode(-1)
        current = dummy_node
        for value in flat_array:
            current.next = ListNode(value)
            current = current.next
        return dummy_node.next
            
        