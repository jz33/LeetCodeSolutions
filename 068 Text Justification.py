'''
68. Text Justification
https://leetcode.com/problems/text-justification/

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and
is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on
the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
             
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
class Solution:
    def pack(self, words: List[str], maxWidth: int) -> str:
        wordsWidth = sum(len(word) for word in words)
        totalSpaceWidth = maxWidth - wordsWidth
        spaceCount = len(words) - 1
        if spaceCount == 0:
            return words[0] + ' ' * totalSpaceWidth
        
        mod = totalSpaceWidth % spaceCount
        if mod == 0:
            spaceWidth = totalSpaceWidth // spaceCount
            return (' ' * spaceWidth).join(words)
        else:
            smallerSpaceWidth = totalSpaceWidth // spaceCount
            biggerSpaceCount = mod
            res = [words[0]]
            for i in range(1, len(words)):
                if i < biggerSpaceCount + 1:
                    res.append(' ' * (smallerSpaceWidth+1))
                else:
                    res.append(' ' * smallerSpaceWidth)
                res.append(words[i])
            return ''.join(res)
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = 0 # words widths + spaces
        leftIndex = 0
        result = []
        for i, word in enumerate(words):
            nextLength = length + 1 + len(word) if length > 0 else len(word)
            if nextLength > maxWidth:
                result.append(self.pack(words[leftIndex : i], maxWidth))
                length = len(word)
                leftIndex = i
            else:
                length = nextLength
        
        lastLine = ' '.join(words[leftIndex:])
        result.append(lastLine + ' ' * (maxWidth - len(lastLine)))
        
        return result
