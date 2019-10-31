'''
557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while
still preserving whitespaceand initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string. 
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        left = 0
        for i, e in enumerate(s):
            if e == ' ':
                res.append(s[left:i][::-1])
                left = i+1      
        res.append(s[left:][::-1])
        return ' '.join(res)
