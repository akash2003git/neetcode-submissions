# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, k):
        kth = None
        while k > 0 and curr:
            kth = curr
            curr = curr.next
            k -= 1
        return kth if k <= 0 else None

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode()
        groupPrev.next = head
        curr = head

        while True:
            kth = self.getKth(curr, k)
            if kth == None:
                break
            
            groupNext = kth.next
            prev = groupNext
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next