'''
381. Insert Delete GetRandom O(1) - Duplicates allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements.
The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''
from random import randint

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {} # {value : set(indexes)}
        self.arr = [] # [value]
        self.ti = -1 # tail index, index to last non-none element, == total - 1
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        existed = val in self.dic
        
        # Put into arr
        self.ti += 1
        if self.ti >= len(self.arr):
            self.arr.append(val)
        else:
            self.arr[self.ti] = val

        # Put into dic
        if existed:
            self.dic[val].add(self.ti)
        else:
            self.dic[val] = set([self.ti])
        
        return not existed        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        existed = val in self.dic
        if existed:
            
            # Get an arbitrary index of val
            pos = self.dic[val].pop()
            
            if pos != self.ti:
                
                # Update arr at pos to last value
                lastVal = self.arr[self.ti]
                self.arr[pos] = lastVal
                
                # Update dic on last value from index self.ti to pos
                self.dic[lastVal].remove(self.ti)
                self.dic[lastVal].add(pos)
            
            # pop last value from arr
            self.arr[self.ti] = None
            self.ti -= 1
        
            # pop val from dic
            if len(self.dic[val])== 0:
                del self.dic[val]

        return existed

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.arr[randint(0,self.ti)]
