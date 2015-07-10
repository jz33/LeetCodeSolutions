'''
Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

No error or exception checking
'''
class Queue:
    def __init__(self):
        self.data = []
        
    def push(self, x):
        self.data.append(x)

    def pop(self):
        d = self.data[0]
        self.data.pop(0)
        return d

    def peek(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0
