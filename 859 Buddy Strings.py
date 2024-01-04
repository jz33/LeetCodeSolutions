'''
859. Buddy Strings
https://leetcode.com/problems/buddy-strings/

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that
i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
    1 <= s.length, goal.length <= 2 * 104
    s and goal consist of lowercase letters.
'''
class Solution:
    def buddyStrings(self, src: str, goal: str) -> bool:
        if len(src) != len(goal):
            return False

        # The first unmatched is the index of the 1st unmatched chars.
        # Initial is None. If found 1st, it is in [0, len(src)]
        # After swapping, it is -1
        firstUnmatched = None
        for i in range(len(src)):
            if src[i] != goal[i]:
                if firstUnmatched == -1:
                    # Already swapped
                    return False
                if firstUnmatched is None:
                    # 1st time unmatched
                    firstUnmatched = i
                else:
                    # 2nd time unmatched
                    if src[i] == goal[firstUnmatched] and src[firstUnmatched] == goal[i]:
                        firstUnmatched = -1
                    else:
                        return False

        if firstUnmatched is None:
            # All same characters. Check if src has duplicates
            return len(set(src)) < len(src)
        return firstUnmatched == -1
