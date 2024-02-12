'''
727. Minimum Window Subsequence
https://leetcode.com/problems/minimum-window-subsequence/

Given strings s1 and s2, return the minimum contiguous substring part of s1,
so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2,
return the empty string "". If there are multiple such minimum-length windows,
return the one with the left-most starting index.

Example 1:

Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.

Example 2:

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""

Constraints:

    1 <= s1.length <= 2 * 104
    1 <= s2.length <= 100
    s1 and s2 consist of lowercase English letters
'''             
class Solution:
    def minWindow(self, source: str, pattern: str) -> str:
        result = ''
        si = 0 # iterator on source
        while si != -1:
            # Keep finding the pattern
            left = None # left index of valid substring, inclusive
            for i, p in enumerate(pattern):
                si = source.find(p, si)
                if si == -1:
                    break
                if i == 0:
                    # Record left index for later rfind
                    left = si
                # Next search should start from next char
                si += 1

            if si != -1:
                # Found, go back to get smallest substring
                right = si # right of the substring, exclusive
                # si is now the last index of the substring +1
                for p in reversed(pattern):
                    si = source.rfind(p, left, si)

                # Now, found minimum substring, source[si : right]
                if result == '' or len(result) > right - si:
                    result = source[si : right]
                # Move si for next search
                si += 1 
        return result
    
sol = Solution()
print(sol.minWindow('abcdebdde', 'bde'))