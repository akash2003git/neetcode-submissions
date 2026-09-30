class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lr, self.mr = Node(), Node()
        self.lr.next, self.mr.prev = self.mr, self.lr

    def insert(self, node: Node):
        prevNode, nextNode = self.mr.prev, self.mr
        node.prev, node.next = prevNode, nextNode
        prevNode.next = nextNode.prev = node

    def remove(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
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
        
