def plus(x,y):
    c = 1
    s = 0
    while c != 0:
        c = (x & y) << 1
        s = x ^ y
        x = c
        y = s
    return s

'''
0 000
1 001
2 010
3 011
4 100
5 101
6 110
7 111
8 1000
'''
def countBits(num):
    ls = [0]*(num+1)
    i = 1
    while i <= num:
        ls[i] = 1
        for j in xrange(1,i):
            if i+j <= num:
                ls[i+j] = ls[j] + 1
        i <<= 1
    return ls

m = 16
print countBits(m)
                                                                                                                                      
