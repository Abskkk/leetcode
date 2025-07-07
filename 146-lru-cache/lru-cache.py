class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            newNode = ListNode(key, value)
            self.hashmap[key] = newNode
            self.insert(newNode)
        else:
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.insert(node)
            if len(self.hashmap) > self.capacity:
                removeNode = self.head.next
                self.remove(removeNode)
                del self.hashmap[removeNode.key]


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)