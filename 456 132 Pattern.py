'''
456. 132 Pattern
https://leetcode.com/problems/132-pattern/

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj,
ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as
input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float('-inf') # This is middle '3', s1 < s3 < s2
        stack = [] # Monotonic stack, descending
        for i in range(len(nums)-1, -1, -1):
            e = nums[i]
            if e < s3:
                # s3 is valid only if there is s2
                return True
            
            while stack and e > stack[-1]:
                s3 = stack.pop()
            stack.append(e)

        return False
