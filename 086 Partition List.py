'''
Partition List
https://leetcode.com/problems/partition-list/
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def fromList(ls):
    if len(ls) == 0 : return None
    head = ListNode(ls[0])
    p = head
    for i in xrange(1,len(ls)):
        p.next = ListNode(ls[i])
        p = p.next
    return head
    
def printList(head):
    while head != None:
        print head.val
        head = head.next

def partition(head, th):
    fake = ListNode(None)
    fake.next = head   
    lt = rt = fake
    while rt.next != None:
        if rt.next.val < th:
            if lt.next == rt.next:
                lt = lt.next
                rt = rt.next
            else:
                t = rt.next
                rt.next = t.next
                t.next = lt.next
                lt.next = t
                lt = t
        else:
            rt = rt.next
    return fake.next

head = fromList([4,1,2,0])
printList(head)
p = partition(head,3)
printList(p)
