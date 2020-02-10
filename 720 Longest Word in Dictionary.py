'''
720. Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/

Given a list of strings words representing an English Dictionary,
find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary.
However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Sort, shorted words go first
        words.sort() 
        
        # The book only contains the "builtable" words
        book = set()
        
        res = ''
        for word in words:
            # Only need to check if word[:-1] is builtable or not,
            # because if word[:-1] is builtable, word[:-2] is also
            # builtable, as book only contains buitable words
            if len(word) == 1 or word[:-1] in book:
                if len(word) > len(res):
                    res = word
                book.add(word)
        return res
     
