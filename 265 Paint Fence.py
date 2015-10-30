'''
Paint Fence
https://leetcode.com/problems/paint-fence/
'''
def numWays(n, k):
    """
    :type n: int, n posts
    :type k: int, k colors
    :rtype: int
    """
    if n == 0: return 0
    if k == 0: return 0
    
    # tuple : (same color, no same color)
    prev = (0,k)
    for i in xrange(1,n):
        curr = (prev[1], (prev[0] + prev[1])*(k-1))
        prev = curr
    return prev[0] + prev[1]
      
n = 5
k = 5
print numWays(n,k)
