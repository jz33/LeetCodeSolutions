'''
527. Word Abbreviation
https://leetcode.com/problems/word-abbreviation/

Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for
every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.

If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used
instead of only the first character until making the map from word to abbreviation become unique.
In other words, a final abbreviation cannot map to more than one original words.

If the abbreviation doesn't make the word shorter, then keep it as original.
Example:

Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
'''
class Solution:
    def getAbbr(self, word: str, prefixCount: int) -> str:
        if prefixCount > len(word) - 3:
            # abcde => ab2e, NOT abc1e
            return word
        
        return word[:prefixCount] + str(len(word) - prefixCount - 1) + word[-1]
        
    def wordsAbbreviation(self, src: List[str]) -> List[str]:    
        result = [self.getAbbr(word, 1) for word in src]
        prefixCountBook = {word : 1 for word in src} # {word : prefixCount}

        for i in range(len(src)):
            while True:
                # Get how many duplicates to result[i]
                # Notice result[i] needs to be included because it needs to expand
                duplicates = [j for j in range(i, len(src)) if result[i] == result[j]]
                if len(duplicates) == 1:
                    break
                    
                for j in duplicates:
                    word = src[j]
                    prefixCount = prefixCountBook[word] + 1
                    result[j] = self.getAbbr(word, prefixCount)
                    prefixCountBook[word] += 1
                    
        return result
