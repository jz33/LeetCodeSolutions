'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lengthOfLongestSubstring(s: str) -> int:
    # Sliding window
        book = {}
        left = 0 # left index of the substring
        maxLength = 0
        for i, e in enumerate(s):
            if e in book:
                # Simply forward the left margin
                # Notice buf[e] can be less than left
                left = max(left, book[e]+1)
            book[e] = i
            maxLength = max(maxLength, i - left + 1)
            
        return maxLength
