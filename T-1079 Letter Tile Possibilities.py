'''
1079. Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/

You have a set of tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: "AAABBC"
Output: 188
 
Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''
class LetterCounter:
    '''
    A simple counter used for words with lowercase or uppercase letters only
    '''
    def __init__(self, word: str):
        arr = [0] * 26
        A = ord('A')
        for e in word:
            arr[ord(e) - A] += 1
        self.arr = arr

    def items(self):
        for i, c in enumerate(self.arr):
            if c > 0:
                yield i, c

class Solution:
    def backtrack(self, ctr: LetterCounter) -> int:
        total = 0
        for k, c in ctr.items():
            # Current combination, +1
            total += 1
            
            # Remove 1 letter, + subroutine result
            ctr.arr[k] -= 1
            total += self.backtrack(ctr)
            ctr.arr[k] += 1
            
        return total
        
    def numTilePossibilities(self, tiles: str) -> int:
        ctr = LetterCounter(tiles)
        return self.backtrack(ctr)
