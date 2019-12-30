'''
358. Rearrange String k Distance Apart
https://leetcode.com/problems/rearrange-string-k-distance-apart/

Given a non-empty string s and an integer k,
rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.

Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.

Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
'''
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # 1. Get the most common char
        ctr = collections.Counter(s)   
        topChar, topCharCount = ctr.most_common(1)[0]
        
        # 2. Build buckets of chars, first char of each bucket is the top char.
        # Fill other chars to buckets
        buckets = [[topChar] for _ in range(topCharCount)]
        bi = 0
        for char, count in ctr.items():
            if char != topChar:
                for _ in range(count):
                    buckets[bi].append(char)
                    bi += 1
                    # If count == topCharCount, fill last bucket, because it has to.
                    # Otherwise, do not fill last bucket, to put the char to next level.
                    if count == topCharCount and bi == len(buckets) or \
                       count < topCharCount and bi == len(buckets) - 1:
                        bi = 0
                        
        # 3. Check buckets. First topCharCount - 1 buckets must have at least k chars
        # Check from back for speed
        if any(len(buckets[i]) < k for i in range(topCharCount-2, -1, -1)):
            return ""
        
        return ''.join(''.join(b) for b in buckets) 
