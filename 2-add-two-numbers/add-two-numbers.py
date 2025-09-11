# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        currentNode = dummyNode
        t1, t2 = l1, l2
        Sum = 0
        carry = 0
        while t1 or t2:
            Sum = carry
            if t1:
                Sum += t1.val
            if t2:
                Sum += t2.val
            nodeVal = Sum % 10
            carry = Sum // 10
            newNode = ListNode(nodeVal)
            currentNode.next = newNode
            currentNode = newNode
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            newNode = ListNode(carry)
            currentNode.next = newNode
            currentNode = newNode
        return dummyNode.next
