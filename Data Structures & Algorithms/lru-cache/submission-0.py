class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prevToRight = self.right.prev
        node.prev = prevToRight
        prevToRight.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prevToNode = node.prev
        nextToNode = node.next
        prevToNode.next, nextToNode.prev = nextToNode, prevToNode

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])
        if len(self.hmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]
                
