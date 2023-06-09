class ListNode:
    def __init__(self, val,key=None,next=None,prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
    

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        start = ListNode(0)
        end = start
        self.p = start
        self.s = start
        for _ in range(capacity-1):
            temp = ListNode(0)
            end.next = temp
            temp.prev = end
            end = end.next

    def get(self, key: int) -> int:
        if key in self.d:
            ret = self.d[key].val
            node = self.d[key]
            nk = self.d[key].key
            if node.next is None:
                return ret
            node.val = node.next.val
            node.key = node.next.key
            node.next.key = nk
            node.next.val = ret
            return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            nk = node.key
            if node.next is None:
                self.d[key].val = value
                return 
            node.val = node.next.val
            node.key = node.next.key
            node.next.key = nk
            node.next.val = value
            self.d[key].val = value
            return
        elif self.p is not None:
                self.p.key = key
                self.p.val = value
                self.d[key] = self.p
                self.d["append"] = self.p
                self.p = self.p.next            
                if self.p is not None:
                    self.p.prev = self.d["append"]   
        else:
            if self.s.key in self.d:
                del self.d[self.s.key]
            temp = self.s
            self.s = self.s.next
            temp = None
            self.p = ListNode(value)
            self.p.prev = self.d["append"]
            self.p.key = key
            self.d[key] = self.p
            self.d["append"] = self.p
            self.p = self.p.next

        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
