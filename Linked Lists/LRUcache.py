"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


class ListNode:
    def __init__(self, val,key=None,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        start = ListNode(1)
        end = start
        self.p = start
        for _ in range(capacity-1):
            temp = ListNode(1)
            end.next = temp
            temp.prev = end
            end = end.next
        self.s = start

    def append(self,node,k):
        if self.p is None:
            if node.prev is None:
                self.s, self.s.prev = self.s.next, None
                node.next, node.prev = None, self.b
                self.b.next = node
                self.p, self.b = node, node
                self.p = self.p.next
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev, node.next = None, None
                self.b.next, node.prev = node, self.b
                self.p, self.b = node, node
                self.p = self.p.next
        elif self.p.key is None:
            if node.prev is None:
                self.s, self.s.prev = self.s.next, None
                node.next.prev = None
                self.b.next = node
                node.prev = self.b
                temp = ListNode(1)
                temp.next = self.p.next
                node.next, temp.prev = temp, node
                self.p, self.b = temp, node
            else:
                node.next.prev, node.prev.next = node.prev, node.next
                self.b.next = node
                node.prev = self.b
                temp = ListNode(1)
                temp.next = self.p.next
                node.next, temp.prev = temp, node 
                self.p, self.b = temp, node
        self.d[k] = node
                
                
    def get(self, key: int) -> int:
        if key in self.d:
            ret = self.d[key].val
            node = self.d[key]
            nk = node.key
            if node.next is None or node.next.key is None:
                return ret
            LRUCache.append(self,node,nk)
            if node.next is None or node.next.key is None:
                return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            nk = node.key
            self.d[key].val = value
            if node.next is None or node.next.key is None:
                return 
            LRUCache.append(self,node,nk)
        elif self.p is not None and self.p.key is None:
                self.p.key = key
                self.p.val = value
                self.d[key] = self.p
                self.b = self.p
                self.p = self.p.next            
                if self.p is not None:
                    self.p.prev = self.b   
        elif self.p is None:
            self.p = ListNode(value)
            self.p.prev = self.b
            self.b.next = self.p
            self.p.key = key
            self.d[key] = self.p
            self.b = self.p
            self.p = self.p.next
            k = self.s.key
            self.s.next.prev = None
            self.s = self.s.next
            if k in self.d:
                del self.d[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
