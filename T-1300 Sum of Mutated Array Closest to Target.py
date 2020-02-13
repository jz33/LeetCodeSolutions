'''
1300. Sum of Mutated Array Closest to Target
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

Given an integer array arr and a target value target,return the integer value such that
when we change all the integers larger than value in the given array to be equal to value,
the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

Example 2:

Input: arr = [2,3,5], target = 10
Output: 5

Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
'''
class Solution:
    def getInsertionPoint(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            midVal = arr[mid]
            if midVal == target:
                return mid
            
            if midVal < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
                 
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        total = sum(arr)
        if total <= target:
            return arr[-1]
        
        # Build prefix arr
        size = len(arr)
        prefix = [0] * (size + 1)
        for i in range(size):
            prefix[i+1] = prefix[i] + arr[i]
        
        value, valueTotal = None, float('inf')        
        left, right = 0, arr[-1]     
        while left <= right:
            mid = left + ((right - left) >> 1)
            ins = self.getInsertionPoint(arr, mid)
            total = prefix[ins] + (size - ins) * mid

            diff = abs(total - target) - abs(valueTotal - target)
            if diff < 0 or diff == 0 and mid < value:
                value = mid
                valueTotal = total
               
            if total < target:
                left = mid + 1
            else:
                right = mid - 1
        return value
