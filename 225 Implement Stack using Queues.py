'''
Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
'''
class Stack(object):
    def __init__(self):
        '''
        Queue can only do "append", "pop(0)"
        '''
        self.data = []
        self.help = []
        
    def push(self, x):
        self.data.append(x)

    def pop(self):
        while len(self.data) != 0:
            self.help.append(self.data.pop(0))
            
        while len(self.help) != 1:
            self.data.append(self.help.pop(0))
        
        self.help.pop(0)

    def top(self):
        while len(self.data) != 0:
            self.help.append(self.data.pop(0))
            
        while len(self.help) != 1:
            self.data.append(self.help.pop(0))
            
        r = self.help.pop(0)
        self.data.append(r)
        return r

    def empty(self):
        return len(self.data) == 0
        
