'''
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
Greedy
'''
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
