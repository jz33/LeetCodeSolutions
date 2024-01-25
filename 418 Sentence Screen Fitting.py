'''
418. Sentence Screen Fitting
https://leetcode.com/problems/sentence-screen-fitting/

Given a rows x cols screen and a sentence represented as a list of strings,
return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged,
and a word cannot be split into two lines.
A single space must separate two consecutive words in a line.

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.

Constraints:
    1 <= sentence.length <= 100
    1 <= sentence[i].length <= 10
    sentence[i] consists of lowercase English letters.
    1 <= rows, cols <= 2 * 104
'''
from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        combined = ' '.join(sentence) + ' '
        combinedSize = len(combined)
        fit = 0 # How many characters from combined are fit so far
        for _ in range(rows):
            # Try fit next row
            fit += cols
            if (combined[fit % combinedSize] == ' '):
                # Can fit 1 more space
                fit += 1
            else:
                # Overflowed current row. Go back to find the nearest space
                while fit > 0 and combined[(fit - 1) % combinedSize] != ' ':
                    fit -= 1                  
        return fit // combinedSize
