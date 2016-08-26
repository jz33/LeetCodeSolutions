'''
Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
from random import randint

DEBUG = True

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []
        self.ti = -1 # tail index, inclusive
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            self.ti += 1
            if self.ti >= len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.ti] = val
            self.dic[val] = self.ti

            if DEBUG: print "inserted", self.arr, self.ti

            return True
        else:
            return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        else:
            pos = self.dic[val]
            self.tailess(pos,val)

            if DEBUG: print "removed", self.arr, self.ti
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        pos = randint(0,self.ti)
        val = self.arr[pos]
        # self.tailess(pos,val) # add if remove elements is required

        if DEBUG: print "getRandom", self.arr, self.ti
        return val
        
    def tailess(self,pos,val):
        if pos != self.ti:
            last = self.arr[self.ti]
            self.arr[pos] = last
            self.dic[last] = pos

        self.arr[self.ti] = None
        self.ti -= 1
        del self.dic[val]


obj = RandomizedSet()

print obj.insert(1)
print obj.remove(2)
print obj.insert(2)
print obj.getRandom()
print obj.remove(1)
print obj.insert(2)
print obj.getRandom()
