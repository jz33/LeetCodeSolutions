'''
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maxLength = 0
        zeros = 0
        left = 0
        for i, e in enumerate(A):
            if e == 0:
                zeros += 1
                while zeros > K:
                    if A[left] == 0:
                        zeros -= 1
                    left += 1
    
            maxLength = max(maxLength, i - left + 1)
        
        return max(maxLength, len(A) - left)
