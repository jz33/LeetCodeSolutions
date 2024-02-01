'''
2659. Make Array Empty
https://leetcode.com/problems/make-array-empty/

You are given an integer array nums containing distinct numbers,
and you can perform the following operations until the array is empty:

    If the first element has the smallest value, remove it
    Otherwise, put the first element at the end of the array.

Return an integer denoting the number of operations it takes to make nums empty.

Example 1:

Input: nums = [3,4,-1]
Output: 5

Operation	Array
1	[4, -1, 3]
2	[-1, 3, 4]
3	[3, 4]
4	[4]
5	[]

Example 2:

Input: nums = [1,2,4,3]
Output: 5

Operation	Array
1	[2, 4, 3]
2	[4, 3]
3	[3, 4]
4	[4]
5	[]

Example 3:

Input: nums = [1,2,3]
Output: 3

Operation	Array
1	[2, 3]
2	[3]
3	[]

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    All values in nums are distinct.
'''
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # Save original value to index mapping
        valueToIndex = { value : index for index, value in enumerate(nums)} # {value : index}
        nums.sort()
        # Even if the array is sorted, it'll take len(nums) to remove all numbers
        result = len(nums)
        for i in range(1, len(nums)):
            # For example [3, 4, -1], sorted => [-1, 3, 4]
            # The element 3,4 they need to be moved to back due to -1,
            # it can see that any value x, if there is a y that comes later than x,
            # all values from x until sorted (len(nums) - i values) needs to be put into back
            if valueToIndex[nums[i]] < valueToIndex[nums[i - 1]]:
                result += len(nums) - i
        return result