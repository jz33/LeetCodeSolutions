/*
386. Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers/

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
*/
class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<Integer>(n);
        int c = 1;
        for (int i = 0; i < n; i++) {
            res.add(c);
            
            if (c * 10 <= n) {
                // 1, 10, 100, 1000, ...
                c *= 10;
            }
            else if (c < n && c % 10 != 9) {
                c++;
            }
            else {
                if (c == n) {
                    c /= 10;
                }
                while (c % 10 == 9) {
                    c /= 10;
                }
                c++;
            }
        }
        return res;
    }
}       
