"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        curr = head
        res = None
        while curr:
            mp[curr] = Node(curr.val)
            if curr == head:
                res = mp[curr]
            curr = curr.next

        curr = head
        while curr:
            node = mp[curr]
            node.next = mp[curr.next] if curr.next else None
            node.random = mp[curr.random] if curr.random else None
            curr = curr.next

        return res