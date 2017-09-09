class Node(object):
    def __init__(self, key = None,val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
            
class LRUCache(object):         
    def __init__(self, cap):
        """
        :type capacity: int
        """
        self.cap = cap
        self.ref = dict() # key : Node
        head = Node() # head.next point to the least recently used element
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail      

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.ref.get(key)
        if n is None: return -1
        if n != self.tail.prev: # if not already the most recently used
            self.extract(n)
            self.append(n)     
        return n.val

    def put(self, key, val):
        """
        :type key: int
        :type val: int
        :rtype: void
        """
        n = self.ref.get(key) # check map first, key can exist
        if n is None: # add
            n = Node(key,val)          
            if len(self.ref) == self.cap: # LRU operation
                p = self.head.next
                self.extract(p)
                del self.ref[p.key]
            self.ref[key] = n
            self.append(n)
        else: # update
            n.val = val
            if n != self.tail.prev: # if not already the most recently used
                self.extract(n)
                self.append(n)         
    
    def extract(self, n):
        """
        :type n: Node
        :rtype: void
        """
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None
    
    def append(self, n):
        """
        :type n: Node
        :rtype: void
        """
        self.tail.prev.next = n
        n.prev = self.tail.prev
        self.tail.prev = n
        n.next = self.tail 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
