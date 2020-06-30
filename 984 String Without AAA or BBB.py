'''
984. String Without AAA or BBB
https://leetcode.com/problems/string-without-aaa-or-bbb/

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 
Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:

Input: A = 4, B = 1
Output: "aabaa"

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B
'''
class Container:
    def __init__(self, countOfA: int, countOfB: int):
        self.values = [['a', countOfA] , ['b', countOfB]]
    
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
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []
        db = Container(A, B)
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
                # Think case like: aabbaa, aabaabaa
                newCount = min(2, secCount) if secCount == topCount else 1
                newChar = secChar
            else:
                newCount = min(2, topCount)
                newChar = topChar
            
            prevChar = newChar
            res += [newChar] * newCount
            db.decrease(newChar, newCount)
                
        return ''.join(res)
