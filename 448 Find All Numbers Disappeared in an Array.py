'''
448 Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums) + 1
    for e in nums:
        real_e = e % n
        nums[real_e - 1] += n # record e
    return [i for i in range(1,n) if nums[i-1] < n]
