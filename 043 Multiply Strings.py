'''
Multiply Strings
https://leetcode.com/problems/multiply-strings/
'''
Zero = ord('0')

class Solution(object):
    
    def charToInt(self, i):
        return ord(i) - Zero;
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))

        for i in xrange(len(num1)-1,-1,-1):
            carry = 0
            for j in xrange(len(num2)-1,-1,-1):
                bit = res[i + j + 1] + self.charToInt(num1[i]) * self.charToInt(num2[j]) + carry
                res[i + j + 1] = bit % 10
                carry = bit / 10;
            res[i] += carry
    
        i = 0
        while i < len(res):
            if res[i] != 0: break
            i += 1
        if i == len(res):
            return "0"
        else:
            return ''.join(str(x) for x in res[i:])
