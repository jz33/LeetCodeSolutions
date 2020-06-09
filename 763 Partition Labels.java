/*
763. Partition Labels
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
*/
class Solution {
    public List<Integer> partitionLabels(String S) {
        HashMap<Character, Integer> book = new HashMap<>();
        for (int i = 0; i < S.length(); ++i) {
            char c = S.charAt(i);
            book.put(c, i);
        }

        int left = 0;
        int last = 0;
        List<Integer> res = new ArrayList<>();
        for (int i = 0 ; i < S.length(); ++i) {
            char c = S.charAt(i);
            last = Math.max(last, book.get(c));
            if (i == last) {
                res.add(i - left + 1);
                left = i + 1;
            }
        }
        return res;
    }
}
