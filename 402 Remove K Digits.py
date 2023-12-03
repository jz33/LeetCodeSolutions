'''
402. Remove K Digits
https://leetcode.com/problems/remove-k-digits/

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
    1 <= k <= num.length <= 105
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # The stack saves digits that are not yet to be removed
        stack = []
        removedCount = 0
        for n in num:
            # If current digit is smaller, delete previous digit
            while stack and removedCount < k and n < stack[-1]:
                stack.pop()
                removedCount += 1
            
            # Now, n >= stack.at(-1). Save current digit, as it might be retained
            # or deleted later, depends on next digit
            if stack or n != '0':
                stack.append(n)
 
        if removedCount < k:
            toDeleteCount = k - removedCount
            # Remove digits from back, and back digits are bigger
            stack = stack[:-toDeleteCount]
        
        return ''.join(stack) if stack else '0'
