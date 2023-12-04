'''
716. Max Stack
https://leetcode.com/problems/max-stack/

Design a max stack data structure that
supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.

void push(int x) Pushes element x onto the stack.

int pop() Removes the element on top of the stack and returns it.

int top() Gets the element on the top of the stack without removing it.

int peekMax() Retrieves the maximum element in the stack without removing it.

int popMax() Retrieves the maximum element in the stack and removes it.
If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.

Constraints:
    -107 <= x <= 107
    At most 105 calls will be made to push, pop, top, peekMax, and popMax.
    There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
'''
from sortedcontainers import SortedDict

class ListNode:
    '''
    Double linked list node
    '''
    def __init__(self, key = None):
        self.key = key
        self.next = None
        self.prev = None
    
    def __lt__(self, that) -> bool:
        return self.key < that.key
    
    def __repr__(self) -> str:
        return '{0} : {1}'.format(id(self), self.key)
    
    def __hash__(self):
        return id(self)

class DoubleLinkedList:
    def __init__(self):
        # Head and tail are placeholders
        head = ListNode(-10000)
        tail = ListNode(50000)
        head.next = tail
        tail.prev = head
        self.head = head 
        self.tail = tail

    def append(self, node: ListNode) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def last(self) -> ListNode:
        return self.tail.prev
    
    def __repr__(self) -> str:
        node = self.head
        rr = []
        while node:
            rr.append('{0} : {1}'.format(id(node), node.key))
            node = node.next
        return ' '.join(rr)
    
class MaxStack:
    def __init__(self):
        self.dll = DoubleLinkedList()
        # Unfortunately, SortedDict does not support duplicate keys
        self.sd = SortedDict() # {key, [node]}

    def push(self, key: int) -> None:
        node = ListNode(key)
        self.dll.append(node)
        self.sd[key] = self.sd.get(key, []) + [node]

    def pop(self) -> int:
        node = self.dll.last()
        
        nodesList = self.sd.get(node.key, None)
        if nodesList:
            # The last node of nodesList must be the last node of dll
            nodesList.pop()
            if not nodesList:
                self.sd.pop(node.key)
    
        self.dll.remove(node)
        return node.key

    def top(self) -> int:
        return self.dll.last().key

    def peekMax(self) -> int:
        # peekitem returns last (key, value) pair
        return self.sd.peekitem()[0]

    def popMax(self) -> int:
        _, nodesList = self.sd.peekitem()
        node = nodesList.pop()
        if not nodesList:
            self.sd.pop(node.key)
        
        self.dll.remove(node)
        return node.key
    
    def debug(self):
        print('dll: {0}, sd: {1}'.format(self.dll, self.sd))

