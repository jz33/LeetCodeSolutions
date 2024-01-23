'''
68. Text Justification
https://leetcode.com/problems/text-justification/

Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
'''
from typing import List

class Solution:
    def fullJustify(self, allWords: List[str], maxWidth: int) -> List[str]:
        wi = 0 # iterator on all words

        def getWordsToPack():
            '''
            Get the words that can fit the line
            '''
            nonlocal wi
            words = []
            wordsWidth = 0 # words width without spaces
            while wi < len(allWords):
                totalWidth = wordsWidth + len(words) # word width + between spaces + a trailing space
                if totalWidth + len(allWords[wi]) > maxWidth:
                    break
                words.append(allWords[wi])
                wordsWidth += len(allWords[wi])
                wi += 1
            return words, wordsWidth
        
        def pack(words: List[str], wordsWidth: int) -> str:
            '''
            Pack the words
            @words: words to pack
            @wordsWith: total words width, without spaces
            '''
            spaceCount = maxWidth - wordsWidth
            # Case 1: only 1 word
            if len(words) == 1:
                return words[0] + ' ' * spaceCount
            
            gapCount = len(words) - 1
            reminder = spaceCount % gapCount
            if reminder == 0:
                # Case 2: distribute space between words evenly
                spaceWidth = spaceCount // gapCount
                return (' ' * spaceWidth).join(words)
            else:
                # Case 3: there will be 2 kinds of spaces with 1 difference
                smallerGapWidth = spaceCount // gapCount
                biggerGapWidth = smallerGapWidth + 1
                biggerGapCount = reminder
                packed = [words[0]]

                for i in range(1, len(words)):
                    # Pack bigger gaps first
                    if i <= biggerGapCount:
                        packed.append(' ' * biggerGapWidth)
                    else:
                        packed.append(' ' * smallerGapWidth)
                    packed.append(words[i])
                return ''.join(packed)
            
        def packLastLine(words: List[str]) -> str:
            wordsAndSpaces = ' '.join(words)
            return wordsAndSpaces + ' ' * (maxWidth - len(wordsAndSpaces))
        
        # Main
        result = []
        while wi < len(allWords):
            words, wordsWidth = getWordsToPack()
            if wi == len(allWords):
                result.append(packLastLine(words))
            else:
                result.append(pack(words, wordsWidth))
        return result
