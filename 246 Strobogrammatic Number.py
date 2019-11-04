'''
Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false
'''
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        for i in range(len(num) // 2 + 1):
            e = num[i]
            if e == '0' or e == '1' or e == '8':
                if num[-(i+1)] != e:
                    return False
            elif e == '6':
                if num[-(i+1)] != '9':
                    return False
            elif e == '9':
                if num[-(i+1)] != '6':
                    return False
            else:
                return False
            
        return True
