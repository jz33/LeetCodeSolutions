'''
716. Max Stack
https://leetcode.com/problems/max-stack/

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
'''
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        maxStack = self.maxStack

        # maxStack[i] is the max value of stack[:i+1]
        if len(maxStack) == 0:
            maxStack.append(x)
        elif maxStack[-1] <= x:
            maxStack.append(x)
        else: # maxStack[-1] > x
            maxStack.append(maxStack[-1])

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        '''
        This question requires to remove max,
        but also retain elements inserted after it
        '''
        x = self.peekMax()
        
        buf = []
        
        # Get all elements after max
        while self.top() != x:
            buf.append(self.pop())
        
        # Pop max
        self.pop()
        
        # Push back all elements after max
        while len(buf) > 0:
            self.push(buf.pop())
        
        return x
