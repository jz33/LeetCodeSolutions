import random
'''
82 Remove Duplicates from Sorted List
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
83 Remove Duplicates from Sorted List II
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

http://stackoverflow.com/questions/280243/python-linked-list#280284
'''
class linked_list_node:
    def __init__(self,rank):
        self.rank = rank
        self.next = None

class linked_list:
    # notice that "head" node is alwasy NOT None
    def __init__(self):
        self.head = linked_list_node(-1)
        self.tail = self.head
        self.size = 0

    def push_back(self, data):
        node = linked_list_node(data)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def dump(self):
        print "size: ", self.size
        node = self.head.next
        while node:
            print node.rank
            node = node.next
    
    # create linked list of given length, random
    def init_rand(self,size,limit = 1):
        if size <= self.size: raise Exception("input size is too small!")
        if limit < 0: limit = -limt
            
        prev = 0
        for i in range(self.size,size):
            if prev <= limit:
                prev = random.randint(prev,limit)
                self.tail.next = linked_list_node(prev)
            else:
                self.tail.next = linked_list_node(limit)
            self.tail = self.tail.next  
        self.size = size
        
    # count size
    def count_size(self):
        size = 0
        node = self.head.next
        while node :
            node = node.next
            size += 1
        self.size = size
        
    # 83
    def removeDuplicates(self):
        if self.size < 2: return
        p = self.head.next
        q = p
        while q.next is not None:
            while q.next is not None and q.next.rank == p.rank:
                q = q.next
            if q != p:
                p.next = q.next
                q.next = None
            p = p.next
            if p is not None: q = p
            
        self.count_size()

    # 84
    def distingush(self):
        if self.size < 2: return
        p = self.head
        q = p
        while q.next is not None:
            while q.next is not None and q.next.rank == p.next.rank:
                q = q.next
            if q != p.next:
                p.next = q.next
                q.next = None
            else:
                p = q
            if p.next is not None: q = p.next
            
        self.count_size()
        # TODO: update self.tail
        
def main():
    lls = linked_list()
    lls.init_rand(2,2)
    lls.dump()
    lls.distingush()
    lls.dump()
    
if __name__ == "__main__":
    main()
