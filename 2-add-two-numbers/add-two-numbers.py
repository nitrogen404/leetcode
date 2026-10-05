# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = value
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_node = ListNode(-1)
        current_node = dummy_node
        t1, t2 = l1, l2
        Sum, carry = 0, 0
        while t1 or t2:
            Sum = carry
            if t1:
                Sum += t1.val
            if t2:
                Sum += t2.val
            
            node_value = Sum % 10
            carry = Sum // 10
            new_node = ListNode(node_value)
            current_node.next = new_node
            current_node = new_node

            if t1: t1 = t1.next
            if t2: t2 = t2.next
        
        if carry:
            new_carry_node = ListNode(carry)
            current_node.next = new_carry_node
        
        return dummy_node.next