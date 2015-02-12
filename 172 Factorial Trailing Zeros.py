import math
'''
172 Factorial Trailing Zeros
https://oj.leetcode.com/problems/factorial-trailing-zeroes/
http://blog.csdn.net/kenden23/article/details/16847887
'''
def factorialTrailingZeros(n):
    if n < 0: return -1
    
    fiveNums = 0
    i = 5
    a = n // i
    while a > 0: 
        fiveNums += a
        i *= 5
        a = n // i 
    return fiveNums
    
def main():
    N = 15
    for i in range(1,N):
        print i
        print math.factorial(i)
        print factorialTrailingZeros(i)
        print
    
    
if __name__ == "__main__":
    main()
