'''
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).
Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 
Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
'''
class MyCircularDeque:

    def __init__(self, capacity: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = capacity
        self.arr = [None] * capacity
        
        # head index, when not empty, should point to first element
        self.head = 0; 
        
        # tail index, when not full, should point to next available slot
        self.tail = 0;

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        head = self.decrease(self.head)
        self.arr[head] = value
        self.head = head
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        tail = self.tail
        self.arr[tail] = value
        self.tail = self.increase(tail)
        return True        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        head = self.head
        self.arr[head] = None
        self.head = self.increase(head)
        return True 
        
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        tail = self.decrease(self.tail)
        self.arr[tail] = None
        self.tail = tail
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.arr[self.head] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.arr[self.decrease(self.tail)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size() == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size() == self.capacity

    def size(self) -> int:
        head = self.head
        tail = self.tail
        if head == tail:
            return 0 if self.arr[head] is None else self.capacity
        elif head < tail:
            return tail - head
        else:
            return self.capacity - head + tail
    
    def increase(self, pointer: int) -> int:
        return (pointer + 1) % self.capacity 
        
    def decrease(self, pointer: int) -> int:
        return (pointer - 1) % self.capacity
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
