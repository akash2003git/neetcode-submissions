class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lR, self.mR = Node(0, 0), Node(0, 0)
        self.lR.next, self.mR.prev = self.mR, self.lR

    def insert(self, node):
        prevNode, nextNode = self.mR.prev, self.mR
        prevNode.next = nextNode.prev = node
        node.next, node.prev = nextNode, prevNode
    
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

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
        
