/*
1247. Minimum Swaps to Make Strings Equal
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings,
which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2: 

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
*/
class Solution {
    public int minimumSwap(String s1, String s2) {
        int size = s1.length();
        
        // Count how many x/y, y/x pairs
        HashMap<String, Integer> counter = new HashMap();
        for (int i = 0 ; i < size; ++i) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            if (c1 == 'x' && c2 == 'y') {
                counter.put("xy", counter.getOrDefault("xy", 0) + 1);
            } else if (c1 == 'y' && c2 == 'x') {
                counter.put("yx", counter.getOrDefault("yx", 0) + 1);
            }
        }
        
        // xy + xy or yx + yx needs 1 swap; xy + yx or yx + xy needs 2 swaps
        int xy = counter.getOrDefault("xy", 0);
        int yx = counter.getOrDefault("yx", 0);
        int res = (xy >> 1) + (yx >> 1);
        if ((xy & 1) != (yx & 1)) {
            return -1;
        }
        
        return (xy & 1) == 0 ? res : res + 2;
    }
}
