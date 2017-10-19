'''
Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
No error or exception checking
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk = [] # stack
        self.rev = [] # reversed stack
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stk.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # pop everything to rev
        if len(self.rev) == 0:
            while len(self.stk) != 0:
                self.rev.append(self.stk.pop())
        # always look from rev
        return self.rev.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.rev) == 0:
            while len(self.stk) != 0:
                self.rev.append(self.stk.pop()) 
        return self.rev[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stk) == 0 and len(self.rev) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
