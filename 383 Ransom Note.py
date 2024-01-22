'''
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters
'''
def buildHistogram(word: str):
    histogram = [0] * 26
    for char in word:
        histogram[ord(char) - ord("a")] += 1
    return histogram
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sourceHistogram = buildHistogram(magazine)
        targetHistogram = buildHistogram(ransomNote)
        for i, count in enumerate(targetHistogram):
            if count > 0:
                sourceCount = sourceHistogram[i]
                if sourceCount < count:
                    return False
        return True
    
'''
Real facebook interview question 20240122
// The Facebook company store sells stickers that say the word “facebook”, we can make posters by cutting and pasting the letters in the word "facebook" to make other words.
// Given a particular source string representing a word on a sticker, write a function that tells me // how many stickers of that string I need in order to make a given target string
// Your function should take in both a source string and target string, and return the number of // stickers.
// source == "facebook", target == "fee": return 2
// source == "facebook", target == "BOO": return 1
// source == "facebook", target == "coffee kebab": return 3
// source == "facebook", target == "booo": return 2
'''
'''
// idea: build histogram of the source + target

// Time Complexity: O(N), N = max(len(source), len(target))
// Memory: O(1), 26 letters
'''

def buildHistogram(s: str):
    histogram = [0] * 26
    for e in s:
        histogram[ord(e.toLower()) - ord('a')] += 1
    return histogram

def getStickerCount(source: str, target: str) -> int:
    sourceHistogram = buildHistogram(source)
    targetHistogram = buildHistogram(target)
    minStickerNeeded = 0
    for i, count in enumerate(targetHistogram):
        if count > 0:
            sourceCount = sourceHistogram[i]
            if sourceCount == 0:
                return -1
            needed = count // sourceCount if count % sourceCount == 0 else count // sourceCount + 1
            minStickerNeeded = max(minStickerNeeded, needed)
    return minStickerNeeded