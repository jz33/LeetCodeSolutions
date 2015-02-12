'''
Climbing Stairs
https://oj.leetcode.com/problems/climbing-stairs/
https://www.codeeval.com/open_challenges/64/

Fibonacci Numbers
Might be extremely awkward if the chosen 
language has no stock MEGA integer implemenation
'''
cache = {}
curr = 0

def fibonacci(n):
    global curr
    if n <= 2:
        return n
    if n <= curr:
        return cache[n]
    else:
        a = cache[curr-1]
        b = cache[curr]
        c = 0
        for x in xrange(curr+1,n+1):
            c = a+b
            a = b
            b = c
            cache[x] = b
        curr = n
        return cache[n]

def main():
    global curr
    cache[1] = 1
    cache[2] = 2
    cache[3] = 3
    curr = 3

    print fibonacci(125)
    
if __name__ == '__main__':
    main()
