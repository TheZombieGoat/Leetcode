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
                self.s = self.s.next
                self.s.prev = None
                print("a")
                node.next = None  
                node.prev = self.b
                self.b.next = node
                self.p = node
                self.b = node
                self.p = self.p.next
                self.d[k] = node
            else:
                print("b") 
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev, node.next = None, None
                self.b.next = node
                node.prev = self.b
                self.p = node
                self.b = node
                self.p = self.p.next
                self.d[k] = node
        elif self.p.key is None:
            if node.prev is None:
                print("c")
                self.s = self.s.next
                self.s.prev = None
                app = self.p.next
                self.s = self.s.next
                node.next.prev = None
                self.b.next = node
                temp = ListNode(1)
                node.next = temp
                temp.next = app 
                self.p = self.p.next
                self.d[k] = node
            else:
                print("d")
                app = self.p.next
                node.next.prev = node.prev
                node.prev.next = node.next
                self.b.next = node
                temp = ListNode(1)
                node.next = temp
                temp.next = app 
                self.p = self.p.next
                self.d[k] = node
                
    def get(self, key: int) -> int:
        if key in self.d:
            ret = self.d[key].val
            node = self.d[key]
            nk = node.key
            if node.next is None or node.next.key is None:
                print("get1")
                return ret
            print("get2", end="")
            LRUCache.append(self,node,nk)
            if node.next is None or node.next.key is None:
                print(" it worked")
            return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            print("key exists",key,value)
            node = self.d[key]
            nk = node.key
            self.d[key].val = value
            if node.next is None or node.next.key is None:
                return 
            LRUCache.append(self,node,nk)
            #self.d[nk] = node
            #self.d[key] = node.next
        elif self.p is not None and self.p.key is None:
                print("p isnt none but key is none",key,value)
                self.p.key = key
                self.p.val = value
                self.d[key] = self.p
                self.b = self.p
                self.p = self.p.next            
                if self.p is not None:
                    self.p.prev = self.b   
        elif self.p is None:
            print("hi",key,value)
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
