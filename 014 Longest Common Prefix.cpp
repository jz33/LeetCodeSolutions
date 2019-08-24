/*
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix
Worst time complexity: O(n), n is sum of all string length
Memory Usage: 8.6 MB, less than 100.00% of C++ online submissions
*/
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs)
    {
        if (strs.size() < 1) return "";
        if (strs.size() < 2) return strs[0];
        
        const auto p = strs[0]; // result prefix
        size_t l = p.size(); // result prefix length

        for (const auto& s : strs)
        {
            l = std::min(l, s.size());
            
            for (size_t j = 0; j < l; ++j)
            {
                if (p[j] != s[j])
                {
                    l = j;
                    break;
                }
            }
        }
        return p.substr(0, l);
    }
};
