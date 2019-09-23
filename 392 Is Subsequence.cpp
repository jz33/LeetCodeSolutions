/*
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t.
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
*/
class Solution {
public:
    bool isSubsequence(string needle, string haystack)
    {
        if (needle.size() == 0)
        {
            return true;
        }

        size_t ni = 0;
        for (auto hc : haystack)
        {
            auto nc =  needle[ni];

            // Use Greedy. As long as a hc matches nc,
            // increase ni, because later matching does not matter
            if (nc == hc)
            {
                ni++;
            }
            if (ni == needle.size())
            {
                return true;
            }
        }
        return false;
    }
};
