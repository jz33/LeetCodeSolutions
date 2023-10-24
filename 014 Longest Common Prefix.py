'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
    
        common = strs[0]
        commonLength = len(common)

        for word in strs[1:]:
            i = 0;
            while i < min(commonLength, len(word)):
                if (common[i] != word[i]):
                    break;
                i += 1
            commonLength = min(commonLength, i);
          
        return common[:commonLength];
