'''
214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"
'''
def kmpTable(needle: str) -> List[str]:
    # T[i] is the length of the longest proper prefix of ndl[:i+1]
    # which is also the suffix of ndl[:i+1]
    # T[0] is always 0
    n_len = len(needle)
    T = [0] * n_len
    
    ll = 0; # The length of the previous longest prefix suffix
    i = 1; # Iterator of T
    while i < n_len:
        if needle[i] == needle[ll]:
            # If current char matches ll-th char from beginning of needle,
            # and because needle[:ll] == needle[i-ll:i],
            # therefore needle[:ll+1] == needle[i-ll:i+1]
            ll += 1
            T[i] = ll;
            i += 1
        elif ll > 0:
            # No match, try to reduce ll to see if matching
            ll = T[ll-1];
        else:
            # No match no matter what, move on
            # T[i] = 0, by default
            i += 1

    return T

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        t = s + '#' + s[::-1]
        kmp = kmpTable(t)

        # By definition of KMP algorithm, kmp[-1] will be
        # the length of longest prefix of twith equals the suffix of t
        lp = kmp[-1]
        return s[lp:][::-1] + s
    
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev[i:]):
                break
        return rev[:i] + s 
