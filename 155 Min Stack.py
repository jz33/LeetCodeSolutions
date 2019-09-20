'''
155 Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = [] # mins is descending array
        
    def push(self, x: int) -> None:
        self.data.append(x)
        
        # Build mins as desceding array.
        # Notice the equal case
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        r = self.data.pop();
        if self.mins and r == self.mins[-1]:
            self.mins.pop()
        return r

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
