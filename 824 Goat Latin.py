'''
824. Goat Latin
https://leetcode.com/problems/goat-latin/

A sentence S is given, composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''
class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, word in enumerate(S.split(' ')):
            goat = None
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                goat = word + 'ma' + 'a' * (i+1)
            else:
                goat = word[1:] + word[0] + 'ma' + 'a' * (i+1)
            res.append(goat)
        return ' '.join(res)
