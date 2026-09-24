class Node:
    
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lR, self.mR = Node(), Node()
        self.lR.next, self.mR.prev = self.mR, self.lR

    def insert(self, node):
        prevNode, nextNode = self.mR.prev, self.mR
        prevNode.next = nextNode.prev = node
        node.prev, node.next = prevNode, nextNode

    def remove(self, node):
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
            lru = self.lR.next
            self.remove(lru)
            del self.cache[lru.key]
        
