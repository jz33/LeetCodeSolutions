'''
Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
'''
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [] # stack
        self.rev = [] # reversed stack
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # pop everything to reversed stack
        if not self.rev:
            while self.stack:
                self.rev.append(self.stack.pop())
                
        # always look from reversed stack
        return self.rev.pop()   

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.rev:
             while self.stack:
                self.rev.append(self.stack.pop()) 

        res = self.rev.pop()
        self.rev.append(res)
        return res
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack and not self.rev
