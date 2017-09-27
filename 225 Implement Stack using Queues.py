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
        while len(self.data) > 1:
            self.help.append(self.data.pop(0))
        r = self.data.pop(0)
        self.data,self.help = self.help,self.data
        return r

    def top(self):
        while len(self.data) > 1:
            self.help.append(self.data.pop(0))
        r = self.data.pop(0)
        self.help.append(r)
        self.data,self.help = self.help,self.data
        return r

    def empty(self):
        return len(self.data) == 0
        
