'''
564. Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"

Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        '''
        For example, 12345, there will be 5 candidates:
        [9999, 12221, 12321, 12421, 100001]
        For 123456: [99999,122221, 123321, 124421, 1000001]
        '''
        width = len(n)
        ori = int(n)
        
        def getpalindrome(i: int):
            nonlocal candidates
            ss = str(i)
            if (width & 1) == 0:
                candidates.append(ss + ss[::-1])
            else:
                candidates.append(ss + ss[:-1][::-1])
                
        # Add smallest and biggest
        candidates = [str(10 ** width + 1), str(10 ** (width - 1) - 1)]
        
        # Add 3 closests
        half = int(n[: (width + 1) // 2])      
        getpalindrome(half - 1)
        getpalindrome(half)
        getpalindrome(half + 1)
        
        return min((c for c in candidates if c != n), key = lambda x: (abs(int(x) - ori)))
