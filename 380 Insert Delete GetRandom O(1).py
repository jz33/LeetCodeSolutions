'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
'''
class RandomizedSet:
    def __init__(self):
        self.dic = {} # {value : index}
        self.arr = [] # [values]

    def insert(self, val: int) -> bool:
        existed = val in self.dic
        if not existed:
            
            # Put into arr
            self.arr.append(val)
            
            # Put into dic
            self.dic[val] = len(self.arr) - 1
        
        return not existed

    def remove(self, val: int) -> bool:
        existed = val in self.dic
        if existed:         
            pos = self.dic[val]
            
            # Swap last value to pos
            if pos != len(self.arr) - 1:               
                lastVal = self.arr[-1]
                self.arr[pos] = lastVal
                
                # Update dic on last value
                self.dic[lastVal] = pos
            
            # pop val from arr
            self.arr.pop()
        
            # pop val from dic
            del self.dic[val]

        return existed  

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)
