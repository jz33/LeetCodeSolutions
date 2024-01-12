'''
996. Number of Squareful Arrays
https://leetcode.com/problems/number-of-squareful-arrays/

An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1

Constraints:
    1 <= nums.length <= 12
    0 <= nums[i] <= 109
'''
import math 

def isSquare(a: int) -> bool:
    root = math.floor(math.sqrt(a))
    return root * root == a

class Solution:
    '''
    Based on 47. Permutations II
    '''
    def numSquarefulPerms(self, nums: List[int]) -> int:
        size = len(nums)
        permsCount = 0

        def topDown(arr: List[int], start: int):
            nonlocal permsCount
            if start == size:
                permsCount += 1
            else:
                for i in range(start, size):
                    if i != start and arr[i] == arr[start]:
                        continue
                    arr[i], arr[start] = arr[start], arr[i]
                    # Can only look back not look ahead, as start + 1 is not swapped yet
                    if start == 0 or isSquare(arr[start-1] + arr[start]):
                        topDown(arr[:], start+1)
 
        topDown(sorted(nums), 0)
        return permsCount