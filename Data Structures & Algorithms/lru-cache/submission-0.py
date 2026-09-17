class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lr, self.mr = Node(0, 0), Node(0, 0)
        self.lr.next, self.mr.prev = self.mr, self.lr

    def insert(self, node):
        prv, nxt = self.mr.prev, self.mr
        prv.next = nxt.prev = node
        node.prev, node.next = prv, self.mr

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.lr.next
            self.remove(lru)
            del self.cache[lru.key]
