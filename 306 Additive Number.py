'''
Additive Number
https://leetcode.com/problems/additive-number/
'''
ZERO = ord('0')

class Solution(object):
    def isAdditiveNumber(self, num):
        size = len(num)
        for i in xrange(1, size / 2 + 1):
            for j in xrange(i + 1, i + (size - i) / 2 + 1):
                if self.check(num[:i], num[i:j], num[j:]): 
                    return True
        return False
        
    def check(self, num1, num2, tail):
        sum = self.addStrings(num1, num2)
        if tail == sum:
            return True
        ls = len(sum)
        if len(tail) <= ls or sum != tail[:ls]:
            return False
        else:
            return self.check(num2, tail[:ls], tail[ls:])

    def addStrings(self,x,y):
        res = []
        carry = 0
        i = len(x)-1
        j = len(y)-1
        while i >= 0 and j >= 0:
            sum = carry + ord(x[i]) - ZERO + ord(y[j]) - ZERO
            carry = sum // 10
            res.append(sum % 10)
            i -= 1
            j -= 1
        while i >= 0:
            sum = carry + ord(x[i]) - ZERO
            carry = sum // 10
            res.append(sum % 10)
            i -= 1
        while j >= 0:
            sum = carry + ord(y[j]) - ZERO
            carry = sum // 10
            res.append(sum % 10)
            j -= 1            
        if carry > 0: 
            res.append(carry);
        return ''.join(str(x) for x in res[::-1])

sol = Solution()
num = "123"
print sol.isAdditiveNumber(num)
