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
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        def pack(line: List[str], wordsWidth: int) -> str:
            '''
            Give a line of words, pack them with spaces
            '''
            totalSpaceWidth = maxWidth - wordsWidth
            if len(line) == 1:
                # Only 1 word, put word first then add spaces
                return line[0] + ' ' * totalSpaceWidth

            spaceCount = len(line) - 1
            mod = totalSpaceWidth % spaceCount
            if mod == 0:
                # Distribute space between words evenly
                spaceWidth = totalSpaceWidth // spaceCount
                return (' ' * spaceWidth).join(line)
            else:
                # There will be 2 kinds of spaces with different space width.
                smallerSpaceWidth = totalSpaceWidth // spaceCount
                biggerSpaceWidth = smallerSpaceWidth + 1
                biggerSpaceCount = mod
                
                result = [line[0]]
                for i in range(1, len(line)):
                    # Pack bigger space first
                    if i <= biggerSpaceCount:
                        result.append(' ' * biggerSpaceWidth)
                    else:
                        result.append(' ' * smallerSpaceWidth)
        
                    result.append(line[i])
    
                return ''.join(result)
        
        line = [] # a line of words waiting to be packed
        wordsWidth = 0 # total word width in line (not including spaces)
        for word in words:
            # Current total width + next word + spaces
            totalNextWidth = (wordsWidth + len(word) + len(line)) if line else len(word)
            
            if totalNextWidth > maxWidth:
                # No more word to add, pack and reset
                result.append(pack(line, wordsWidth))
                line = [word]
                wordsWidth = len(word)
            else:
                # Add current word to line
                line.append(word)
                wordsWidth += len(word)
        
        # Last line
        lastLine = ' '.join(line)
        result.append(lastLine + ' ' * (maxWidth - len(lastLine)))
        
        return result
