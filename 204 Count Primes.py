import sys
'''
Count Primes
https://leetcode.com/problems/count-primes/
Regular Eratosthenes method
'''
def eratosthenes(x):
    if x < 2: return 0
    
    bc = [0 for i in xrange(0,x)];
    counter = 0;
    
    bc[0] = 1; # 1
    bc[1] = 1;
    for i in xrange(1,x):
        if bc[i] == 0:
            counter += 1;
            
            j = i * i
            while j < x:
                bc[j] = 1
                j += i
 
    return counter;

print eratosthenes(int(sys.argv[1]))
