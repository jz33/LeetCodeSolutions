'''
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.
For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.
 
Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]

Constraints:
    1 <= strings.length <= 200
    1 <= strings[i].length <= 50
    strings[i] consists of lowercase English letters.
'''
def getHash(word: str) -> str:
    '''
    Get the hash value by shitfing until first letter is 'a'
    '''
    diff = ord(word[0]) - ord('a')

    def rotate(char: str) -> str:
        newCode = ord(char) - diff
        if newCode < ord('a'):
            newCode += 26
        return chr(newCode)

    return ''.join(map(lambda c : rotate(c), word))

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = {} # {hash : [words]}
        for word in strings:
            hash = getHash(word)
            group[hash] = group.get(hash, []) + [word]
        return group.values()
