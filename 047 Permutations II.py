'''
47. Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
'''
class Solution:
    '''
    Recursive
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        perms = []
        def topDown(arr: List[int], start: int):
            if start == size - 1: # Or start == size
                perms.append(arr)
            else:
                for i in range(start, size):
                    # This is the added line comparing to 46. Permutations 
                    if i != start and arr[i] == arr[start]:
                        continue
                    arr[i], arr[start] = arr[start], arr[i]
                    topDown(arr[:], start + 1)
                    
        topDown(sorted(nums), 0)
        return perms

class Solution2:
    '''
    Iterative
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # This idea is to incrementally build the permuations by each element:
        # insert e onto all positions of previous permutation
        perms = [[]]      
        for e in nums:
            nextPerms = []
            for row in perms:
                for i in range(len(row) + 1):
                    nextPerms.append(row[:i] + [e] + row[i:])
                    # Above line inserts an e before row[i]. If row[i] == e,
                    # then inserting e after row[i] will cause duplicate
                    if i < len(row) and row[i] == e: break 
            perms = nextPerms
        return perms

