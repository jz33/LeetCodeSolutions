'''
415. Add Strings
https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
      i1 = len(num1) - 1
      i2 = len(num2) - 1
      accumulation = 0
      result = []

      def compute(v1, v2):
        nonlocal i1, i2, accumulation
        total = (0 if not v1 else int(v1)) + (0 if not v2 else int(v2)) + accumulation
        if total > 9:
            accumulation = 1
            total -= 10
        else:
            accumulation = 0
        result.append(total)
        if v1 is not None:
            i1 -= 1
        if v2 is not None:
            i2 -= 1

      while i1 >= 0 and i2 >= 0:
          compute(num1[i1], num2[i2])
      while i1 >= 0:
          compute(num1[i1], None)
      while i2 >= 0:
          compute(None, num2[i2])
      if accumulation != 0:
          compute(None, None)
      return ''.join(map(lambda i : str(i), result[::-1]))
