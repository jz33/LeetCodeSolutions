'''
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/

Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
'''
from random import randint

def getInsertionPoint(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def __init__(self, w: List[int]):
        # prefix sums
        '''
        Compute prefix sums array, for example,
        [2,3,4] => [2,5,9], which means,
        1-2 => 0, 3-5 => 1, 6-9 => 2
        '''
        accu = [0] * len(w)
        accu[0] = w[0]
        for i in range(1, len(w)):
            accu[i] = accu[i-1] + w[i]
        self.accu = accu

    def pickIndex(self) -> int:
        target = randint(1, self.accu[-1])
        return getInsertionPoint(self.accu, target)
