class Node:
    '''
    Double linked list node
    '''
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail

    def append(self, node: Node):
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        node.next.prev = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {} # key : Node
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        n = self.keyToNode.get(key)        
        if not n:
            return -1
          
        self.dll.remove(n)
        self.dll.append(n) 
        return n.val

    def put(self, key: int, value: int) -> None:
        node = self.keyToNode.get(key)
        if node:
             # update
            node.val = value
            self.dll.remove(node)
            self.dll.append(node)
        else:
            # add
            node = Node(key, value) 
            
            if len(self.keyToNode) == self.capacity:
                leastUsed = self.dll.head.next
                self.dll.remove(leastUsed)
                del self.keyToNode[leastUsed.key]
                
            self.keyToNode[key] = node
            self.dll.append(node)