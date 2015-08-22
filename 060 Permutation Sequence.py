'''
Permutation Sequence
https://oj.leetcode.com/problems/permutation-sequence/
'''
ERROR = ""

def permutationCount(n ,k):
    '''
    Get permutation count of P(n,k)
    '''
    if k > n or n < 0 or k < 0 : 
        return -1;

    r = 1;
    lowerBound = n - k;
    while n > lowerBound:
        r *= n;
        n -= 1;
    return r;

def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    if n < 0 or k < 0: 
        return ERROR
        
    arr = [0] * n;
    for i in xrange(0,n): 
        arr[i] = i + 1;

    fact = 1 #factorial
    for i in xrange(2,n+1): 
        fact *= i

    k -= 1
    res = [0] * n
    for i in xrange(n,0,-1):
        fact /= i
        r = k / fact
        res[n - i] = arr[r]
        arr.remove(arr[r]) 
        k %= fact
        
    return "".join(str(e) for e in res)

i = 4;
n = 4;
full = permutationCount(n,n);
for i in xrange(0, full): 
    print getPermutation(n,i);
