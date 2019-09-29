'''
937 Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def cmp_str(a: str, b: str) -> int:
    'Convert string comparison result to int'
    if a < b:
        return -1
    if a > b:
        return 1
    return 0
    
class Solution:
    def isDigitLog(self, a: str):
        i = a.index(' ') + 1
        d = ord(a[i])
        return ord('0') <= d and d <= ord('9')
        
    def compLetterLogs(self, a: str, b: str) -> int:
        wsa = a.split(' ')
        wsb = b.split(' ')
        i = 1
        while i < min(len(wsa), len(wsb)):
            wa = wsa[i]
            wb = wsb[i]
            cc = cmp_str(wa, wb)
            if cc != 0:
                return cc
            i += 1
        
        if i == len(wsa):
            return -1
        if i == len(wsb):
            return 1
  
        return cmp_str(wsa[0], wsb[0])
    
    def comp(self, a: str, b: str) -> int:
        isDa = self.isDigitLog(a)
        isDb = self.isDigitLog(b)

        if isDa and isDb:
            return 0
        if isDa:
            return 1
        if isDb:
            return -1

        cc = self.compLetterLogs(a, b)
        return cc
        
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = cmp_to_key(self.comp))
