'''
Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

No error or exception checking
'''
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        self.help = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)

    # @return nothing
    def pop(self):
        while len(self.data) != 0:
            self.help.append(self.data.pop())
            
        self.help.pop()
        
        while len(self.help) != 0:
            self.data.append(self.help.pop())

    # @return an integer
    def peek(self):
        while len(self.data) != 1:
            self.help.append(self.data.pop())
            
        d = self.data.pop()
        self.data.append(d)
        
        while len(self.help) != 0:
            self.data.append(self.help.pop())
        return d
        
    # @return an boolean
    def empty(self):
        return len(self.data) == 0
