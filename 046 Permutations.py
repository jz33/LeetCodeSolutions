'''
46. Permutations
https://leetcode.com/problems/permutations/

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
'''
class Solution:
    '''
    Recursive
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        perms = []
        def topDown(arr: List[int], start: int):
            if start == size - 1:
                perms.append(arr)
            else:
                for i in range(start, size):
                    arr[i], arr[start] = arr[start], arr[i]
                    # deepcopy the array
                    topDown(arr[:], start + 1)
                    
        topDown(sorted(nums), 0)
        return perms

class Solution:
    '''
    Iterative
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        # The idea is to incrementally build the permuations by each element:
        # insert e onto all positions of previous permutation
        perms = [[]]      
        for e in nums:
            nextPerms = []
            for row in perms:
                for i in range(len(row) + 1):
                    nextPerms.append(row[:i] + [e] + row[i:])
            perms = nextPerms
        return perms
