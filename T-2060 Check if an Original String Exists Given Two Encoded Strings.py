'''
2060. Check if an Original String Exists Given Two Encoded Strings
https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

An original string, consisting of lowercase English letters,
can be encoded by the following steps:

    Arbitrarily split it into a sequence of some number of non-empty substrings.
    
    Arbitrarily choose some elements (possibly none) of the sequence,
    and replace each with its length (as a numeric string).
    
    Concatenate the sequence as the encoded string.

For example, one way to encode an original string "abcdefghijklmnop" might be:

    Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
    Choose the second and third elements to be replaced by their lengths, respectively.
    The sequence becomes ["ab", "12", "1", "p"].
    Concatenate the elements of the sequence to get the encoded string: "ab121p".

Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive),
return true if there exists an original string that could be encoded as both s1 and s2.
Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

Example 1:

Input: s1 = "internationalization", s2 = "i18n"
Output: true
Explanation: It is possible that "internationalization" was the original string.
- "internationalization" 
  -> Split:       ["internationalization"]
  -> Do not replace any element
  -> Concatenate:  "internationalization", which is s1.
- "internationalization"
  -> Split:       ["i", "nternationalizatio", "n"]
  -> Replace:     ["i", "18",                 "n"]
  -> Concatenate:  "i18n", which is s2

Example 2:

Input: s1 = "l123e", s2 = "44"
Output: true
Explanation: It is possible that "leetcode" was the original string.
- "leetcode" 
  -> Split:      ["l", "e", "et", "cod", "e"]
  -> Replace:    ["l", "1", "2",  "3",   "e"]
  -> Concatenate: "l123e", which is s1.
- "leetcode" 
  -> Split:      ["leet", "code"]
  -> Replace:    ["4",    "4"]
  -> Concatenate: "44", which is s2.

Example 3:

Input: s1 = "a5b", s2 = "c5b"
Output: false
Explanation: It is impossible.
- The original string encoded as s1 must start with the letter 'a'.
- The original string encoded as s2 must start with the letter 'c'.

Constraints:
    1 <= s1.length, s2.length <= 40
    s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters only.
    The number of consecutive digits in s1 and s2 does not exceed 3.
'''
"""
Refer: https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/solutions/4326369/java-memoization-explained/
"""

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def rec(x: int, y: int, cover: int) -> bool:
            """
            @x: iterator on s1
            @y: iterator on s2
            @cover: when negative, a num on s1 can covers some chars in s2;
            when positive, a num on s2 covers come chars in s1
            """
            if x == len(s1) and y == len(s2):
                # Both iterator reached end, no cover, good
                return cover == 0
            if x < len(s1) and s1[x].isdigit():
                # Check all possible cases on a num
                num = 0
                i = x
                while i < len(s1) and s1[i].isdigit():
                    num = num * 10 + int(s1[i])
                    if rec(i + 1, y, cover - num):
                        return True
                    i += 1
                return False
            if y < len(s2) and s2[y].isdigit():
                # Check all possible cases on a num
                num = 0
                i = y
                while i < len(s2) and s2[i].isdigit():
                    num = num * 10 + int(s2[i])
                    if rec(x, i + 1, cover + num):
                        return True
                    i += 1
                return False
            if cover > 0 and x < len(s1):
                # Only chars, try move by cover
                return rec(x + 1, y, cover - 1)
            if cover < 0 and y < len(s2):
                # Only chars, try move by cover
                return rec(x, y + 1, cover + 1)
            if cover == 0 and x < len(s1) and y < len(s2) and s1[x] == s2[y]:
                # Only chars, no cover, try move both
                return rec(x + 1, y + 1, cover)

            return False

        return rec(0, 0, 0)
