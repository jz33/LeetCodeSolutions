from typing import List, Tuple
'''
https://leetcode.com/discuss/interview-question/456785/Google-or-Onsite-or-Two-Finger-Typing
https://leetcode.com/playground/xadqhiQo

Location: Seattle

The problem is you are given a word and you need to type the word with only 2 fingers.
Each key rests at a coordinate [i,j] and the distance between them is absolute value
of the differencesbetween their components |i1 - i2| + |j1 - j2|.
Compute the minimum distance you would have to travel between the points.

Keyboard Layout

ABCDEF
GHIJKL
MNOPQR
STUVWX
YZ

Your initial positions are considered free so don't count towards your total distance.
Your 2 fingers do NOT have to start at the first letter or the first 2 letters.

Example:

CAKE
Minimum would start at C & K with a total distance of 3.
'''
def toInt(c: str) -> int:
    return ord(c) - ord('A')

def toChr(i: int) -> str:
    return chr(i + ord('A'))

class Board:
    def __init__(self, keyboard):
        points = {} # {char : point}
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                points[keyboard[i][j]] = (i,j)

        self.points = points

    def dist(self, c1: str, c2: str) -> int:
        points = self.points
        return abs(points[c1][0] - points[c2][0]) + abs(points[c1][1] - points[c2][1]) 


class Solution:
    def __init__(self, keyboard):
        self.board = Board(keyboard)

    def dist(self, c1: str, c2: str) -> int:
        return self.board.dist(c1, c2)

    def twoFingerTyping(self, word: str) -> int:
        # dp[j] is the minimum cost when last finger ends at j
        dp = [0] * 26

        for i in range(1, len(word)):
            newDp = [0] * 26
            for j in range(26):

                # Set new finger onto word[i], at dp[word[i]], no added cost, because old finger does't need to move.
                # For dp[j] places other than word[i], we have to move old finger from word[i-1] to word[i],
                # then set new finger onto this other place.
                newDp[j] = dp[j] if j == toInt(word[i]) else dp[j] + self.dist(word[i], word[i-1])   

                # An alternative way is to set new finger onto word[i-1], and move old finger from anywhere
                # to word[i]
                if j == toInt(word[i-1]):
                    newDp[j] = min(newDp[j], min(dp[k] + self.dist(toChr(k), word[i]) for k in range(26)))

            dp = newDp
  
        return min(dp)


keyboard = [
            'ABCDEF',
            'GHIJKL',
            'MNOPQR',
            'STUVWX',
            'YZ']
for row in keyboard:
    print(row)

sol = Solution(keyboard)
cases = [
("CAKE", 3),
("ABZ", 1),
("ABXZ", 5),
("ASBTCU", 4),
("ASGTCU", 6),
]
for src, expected in cases:
    print(src, expected, sol.twoFingerTyping(src))
