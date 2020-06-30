'''
1405. Longest Happy String
https://leetcode.com/problems/longest-happy-string/

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a',
at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.

s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".
 
Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''
class Container:
    def __init__(self, countOfA: int, countOfB: int, countOfC: int):
        self.values = [['a', countOfA] , ['b', countOfB], ['c', countOfC]]
    
    def getTop(self):
        return max(self.values, key = lambda t : t[1])
    
    def getTopExcept(self, char: str):
        return max((t for t in self.values if t[0] != char), key = lambda t : t[1])
    
    def decrease(self, char: str, count: int):
        for i in range(len(self.values)):
            tup = self.values[i]
            if tup[0] == char:
                tup[1] -= count
                break
    
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        Similar to 984. String Without AAA or BBB
        '''
        res = []
        db = Container(a, b, c)
        prevChar = ''
        while True:
            newChar, newCount = None, 0 # to add to result
            topChar, topCount = db.getTop()
            if topCount == 0:
                break
            if topChar == prevChar:
                secChar, secCount = db.getTopExcept(topChar)
                if secCount == 0:
                    break
                
                # Determine how many second char needs to append
                # Think case like: aabaacaa, aabbaaccaa
                newCount = min(2, secCount) if secCount == topCount else 1
                newChar = secChar
            else:
                newCount = min(2, topCount)
                newChar = topChar
            
            prevChar = newChar
            res += [newChar] * newCount
            db.decrease(newChar, newCount)
                
        return ''.join(res)
