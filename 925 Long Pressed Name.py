'''
925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/

Your friend is typing his name into a keyboard.
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        '''
        Try do with O(1) extra space
        '''
        i,j = 0,0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if i == 0:
                    '''
                    ab
                    bbb
                    '''
                    return False
                elif name[i] == name[i-1]:
                    '''
                    aaa
                    aab
                    '''
                    return False
                elif typed[j] != typed[j-1]:
                    '''
                    ab
                    aac
                    '''
                    return False
                else:
                    '''
                    ab
                    aaab
                    '''
                    j += 1
        return i == len(name)
