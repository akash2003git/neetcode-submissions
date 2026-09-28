# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, node, k):
        kth = node
        while kth and k > 0:
            kth = kth.next
            k -= 1
        return kth

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = gP = ListNode(0, head)
        while True:
            kth = self.getKth(gP, k)
            if not kth:
                break
            gN = kth.next

            prev, curr = gN, gP.next
            while curr != gN:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = gP.next
            gP.next = kth
            gP = tmp

        return dummy.next