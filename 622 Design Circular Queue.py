'''
622. Design Circular Queue
https://leetcode.com/problems/design-circular-queue/

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull
'''
class MyCircularQueue:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        # head index, when not empty, should point to first element
        self.head = 0
        # tail index, when not full, should point to next available slot
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        tail = self.tail
        self.arr[tail] = value
        self.tail = self.__forward(tail)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        head = self.head
        self.arr[head] = None
        self.head = self.__forward(head)
        return True 

    def Front(self) -> int:
        return self.arr[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.arr[self.__backward(self.tail)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.__size() == 0

    def isFull(self) -> bool:
        return self.__size() == self.capacity
    
    def __size(self) -> int:
        head = self.head
        tail = self.tail
        if head == tail:
            # Either empty or full
            return 0 if self.arr[head] is None else self.capacity
        elif head < tail:
            return tail - head
        else: # head > tail
            return self.capacity - head + tail
    
    def __forward(self, pointer: int) -> int:
        return (pointer + 1) % self.capacity 
    
    def __backward(self, pointer: int) -> int:
        return (pointer - 1) % self.capacity
