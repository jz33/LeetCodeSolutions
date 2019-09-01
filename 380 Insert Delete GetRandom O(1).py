'''
Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {} # {value : index}
        self.arr = [] # [value]
        self.ti = -1 # tail index, index to last non-none element, == total - 1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        existed = val in self.dic
        if not existed:
            # Put into arr
            self.ti += 1
            if self.ti >= len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.ti] = val

            # Put into dic
            self.dic[val] = self.ti
        
        return not existed 
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        existed = val in self.dic
        if existed:
            
            # Get last index of val
            pos = self.dic[val]
            
            if pos != self.ti:
                # Swap last value to pos
                lastVal = self.arr[self.ti]
                self.arr[pos] = lastVal
                # Update dic on last value
                self.dic[lastVal] = pos
            
            # pop val from arr
            self.arr[self.ti] = None
            self.ti -= 1
        
            # pop val from dic
            del self.dic[val]

        return existed  

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[randint(0,self.ti)]        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
