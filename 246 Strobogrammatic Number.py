'''
246. Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true

Example 2:

Input: num = "88"
Output: true

Example 3:

Input: num = "962"
Output: false

Constraints:
    1 <= num.length <= 50
    num consists of only digits.
    num does not contain any leading zeros except for zero itself.
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
