/*
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
*/
class Solution {
    public int firstUniqChar(String s) {
        int size = s.length();
        HashMap<Character, Integer> seen = new HashMap();
        
        for (int i = 0; i < size; ++i) {
            char c = s.charAt(i);
            if (seen.containsKey(c)) {
                seen.put(c, size);
            } else{
                seen.put(c, i);
            }
        }
        
        int minIndex = size;
        for (Integer i : seen.values()) {
            minIndex = Math.min(minIndex, i);
        }
        
        return minIndex == size ? -1 : minIndex;
    }
}
