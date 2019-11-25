'''
1165. Single-Row Keyboard
https://leetcode.com/problems/single-row-keyboard/

There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 

Example 2:

Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73
'''
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        book = [None] * 26
        for i, key in enumerate(keyboard):
            book[ord(key) - ord('a')] = i
           
        total = 0
        i = 0
        for char in word:
            j = book[ord(char) - ord('a')]
            total += abs(i-j)
            i = j
        return total
