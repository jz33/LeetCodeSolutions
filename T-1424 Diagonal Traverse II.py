'''
1424. Diagonal Traverse II
https://leetcode.com/problems/diagonal-traverse-ii/

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i].length <= 105
    1 <= sum(nums[i].length) <= 105
    1 <= nums[i][j] <= 105
'''
from collections import defaultdict

class Solution:
    '''
    Direct iterate on matrix diagonally. Problems:
    1. Hard to figure out the indexes;
    2. Will iterate a lot empty cells
    '''
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        rowCount = len(nums)
        colCount = len(max(nums, key=len))
        diagonalCount = rowCount + colCount - 1

        for d in range(diagonalCount):
            for r in range(min(d, rowCount-1), max(d - colCount, -1), -1):
                c = d - r
                if c < len(nums[r]):
                    result.append(nums[r][c])

        return result
    
class Solution:
    '''
    Simpler grouping solution, no need to go to empty cells
    '''
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list) # { diagonalIndex : [values] }
        for ri in range(len(nums)-1, -1, -1):
            for ci in range(len(nums[ri])):
                diagonalIndex = ri + ci
                diagonals[diagonalIndex].append(nums[ri][ci])
        
        result = []
        for d in range(len(diagonals.keys())):
            result += diagonals[d]
        return result
    
mat = [
[14,12,19,16,9],
[13,14,15,8,11],
[11,13,1]
]

output = [14,13,12,11,14,19,13,15,16,1,8,9]
expected = [14,13,12,11,14,19,13,15,16,1,8,9,11]

