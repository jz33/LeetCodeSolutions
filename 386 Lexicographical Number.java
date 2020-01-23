/*
386. Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers/

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
*/
class Solution {
    // This is essentially preorder traversal on n-ary tree
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<Integer>(n);
        int c = 1;
        for (int i = 0; i < n; i++) {
            res.add(c);
            
            if (c * 10 <= n) {
                // Go deep to left branchs, e.g., 1, 10, 100, 1000, ...
                c *= 10;
            }
            else if (c < n && c % 10 != 9) {
                // Go though all numbers in 1 node, e.g., 101, 102, 103, ...
                // Make sure not go out of bound (the '9')
                c++;
            }
            else {
                // Go back to a parent
                if (c == n) {
                    c /= 10;
                }
                // Make sure numbers in this node are not exhausted
                while (c % 10 == 9) {
                    c /= 10;
                }
                // Go to sibling
                c++;
            }
        }
        return res;
    }
}    
