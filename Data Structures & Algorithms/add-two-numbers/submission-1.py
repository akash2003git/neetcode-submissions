# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l2.val == 0:
            return ListNode()

        n1, m1, curr = 0, 1, l1
        while curr:
            n1 += curr.val * m1
            m1 *= 10
            curr = curr.next
        
        n2, m2, curr = 0, 1, l2
        while curr:
            n2 += curr.val * m2
            m2 *= 10
            curr = curr.next

        res = n1 + n2
        prev = head = ListNode()
        while res > 0:
            d = res % 10
            res = res // 10
            node = ListNode(d)
            prev.next = node
            prev = node

        return head.next