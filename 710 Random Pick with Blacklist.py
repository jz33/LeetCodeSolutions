'''
710. Random Pick with Blacklist
https://leetcode.com/problems/random-pick-with-blacklist/

Given a blacklist B containing unique integers from [0, N),
write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
'''
from random import randrange

class Solution:
    __slot__ = 'total', 'mapper'
    
    def __init__(self, N: int, blacklist: List[int]):
        '''
        Since N is very big, blacklist is relatively small,
        use a dict to hold the mapping from blacklisted number to
        mapped number. Mapper number can choose from N - 1 backwardsly.
        Notice this method introduces contains bias.
        The non-bias way is to call randrange continuously until result is
        not blacklisted
        '''
        total = N - len(blacklist) # total non-blacklisted numbers
        bound = N - 1 # the upper bound the blacklisted number can mapped to
        blackset = set(blacklist)
        mapper = {}
        for b in blacklist:
            if b < total:
                while bound in blackset:
                    bound -= 1
                mapper[b] = bound
                bound -= 1

        self.mapper = mapper
        self.total = total
      
    def pick(self) -> int:
        r = randrange(0, self.total)
        t = self.mapper.get(r)
        return t if t is not None else r          
