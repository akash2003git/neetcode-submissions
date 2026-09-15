# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next

        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(total - n):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next