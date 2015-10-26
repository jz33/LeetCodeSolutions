'''
Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/
'''
def isStrobogrammatic(num):
    length = len(num)
    for i in xrange(0, length / 2 + 1):
        e = num[i]
        if e == '0' or e == '1' or e == '8':
            if num[length - 1 - i] != e:
                return False
        elif e == '6':
            if num[length - 1 - i] != '9':
                return False
        elif e == '9':
            if num[length - 1 - i] != '6':
                return False
        else:
            return False
    return True
    
num = "61196119"
print isStrobogrammatic(num)
