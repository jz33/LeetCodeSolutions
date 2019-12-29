'''
949. Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits/

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.
Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
'''
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        # Find hours from largest
        for hr in range(23,-1,-1):
            digits = copy.deepcopy(A)
            d0 = hr // 10
            d1 = hr % 10 
            
            try:
                digits.remove(d0)
                digits.remove(d1)
            except ValueError:
                # If value not in list, Python raises ValueError
                continue
            
            prefix = str(d0) + str(d1) + ":"
            
            # Find minutes
            m0 = digits[0] * 10 + digits[1]
            m1 = digits[1] * 10 + digits[0]
            if m0 < 60 and m1 < 60:
                return prefix + '{0:02d}'.format(max(m0, m1))
            elif m0 < 60:
                return prefix + '{0:02d}'.format(m0)
            elif m1 < 60:
                return prefix + '{0:02d}'.format(m1)
            
        return ''
