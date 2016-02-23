import random,sys
'''
155 Min Stack
https://oj.leetcode.com/problems/min-stack/

Use 2 stacks
'''
class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.contents = []
        self.minimums = []

    # @param x, an integer
    # @return an integer
    def push(self, e):
        self.contents.append(e)
        if len(self.minimums) == 0 or e <= self.minimums[-1]:
            self.minimums.append(e)

    # @return nothing
    def pop(self):
        if len(self.contents) == 0:
            raise Exception("len(self.contents) == 0")
        
        e = self.contents.pop()
        if e == self.minimums[-1]:
            self.minimums.pop()
        return e
    
    # @return an integer
    def top(self):
        if len(self.contents) == 0:
            raise Exception("len(self.contents) == 0")      
        return self.contents[-1]

    # @return an integer
    def getMin(self):
        if len(self.minimums) == 0:
            raise Exception("len(self.minimums) == 0")   
        return self.minimums[-1]
        
