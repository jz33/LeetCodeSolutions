/*
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/
class Solution {
public:
    std::vector<std::string> generateParenthesis(int n) {
        m_bound = n;
        m_pool.clear();
        dfs("", 0, 0);
        return m_pool;
    }
    
private:
    void dfs(std::string row, int left, int right) {
        if (left == right && left == m_bound) {
            m_pool.emplace_back(row);
        }
        
        if (left < m_bound) {
            dfs(row + '(', left + 1, right);
        }
        
        if (right < left) {
            dfs(row + ')', left, right + 1);
        }
    }
    
    int m_bound = 0;
    std::vector<std::string> m_pool;
};
