def PermsIterative(iterable, r = None):
    '''
    Based on recursive method
    '''
    n = len(iterable)
    r = n if r is None else r
    if r > n:
        return
    pool = range(n)
    stack = []
    l = 0 # level
    s = 0 # swap index
    while s < n or len(stack) > 0:
        if l + 1 == r:
            yield tuple(iterable[pool[k]] for k in xrange(n))
            # go up
            l,s = stack.pop()
            pool[l],pool[s] = pool[s],pool[l]
            s += 1
        elif s == n:
            # go up
            l,s = stack.pop()
            pool[l],pool[s] = pool[s],pool[l]
            s += 1
        else:
            # go down
            pool[l],pool[s] = pool[s],pool[l]
            stack.append((l,s))
            l += 1
            s = l

from random import randint
from copy import deepcopy

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori
        
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.ori)
        res = deepcopy(self.ori)   
        for i in xrange(n):
            j = randint(i,n-1)
            res[i],res[j] = res[j],res[i]
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
