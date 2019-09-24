/*
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
*/

import java.math.BigInteger;

class Solution {
    private final int[] PRIMES = new int[]{2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107};
    
    private BigInteger computeHash(String s) {
        BigInteger b = new BigInteger("1");
        for (char e : s.toCharArray()) {
            b = b.multiply(BigInteger.valueOf(PRIMES[e - 'a']));
        }
        return b;
    }
    
    public boolean isAnagram(String s, String t) {
        BigInteger h0 = computeHash(s);
        BigInteger h1 = computeHash(t);
        return h0.equals(h1);
    }
}
