def longestPalindrome(s: str) -> str:
    '''
    A simple DP approach
    For example:
    b a b a d
    1 1 1 1 1
     0 0 0 0
      1 0 0 
       0 0
        0
    Where dp[i][j] means whether s[i:j+1] is palindromic or not
    '''
    N = len(s)
    dp = [[False] * N for i in range(N)]

    # Result
    resLeft = 0
    resRight = 0 # inclusive
    foundInThisSize = False
    
    # Initialize substring size = 1 and 2 cases
    for i in range(N):
        dp[i][i] = True
 
    for i in range(N-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            if not foundInThisSize:
                resLeft = i
                resRight = i + 1
                foundInThisSize = True
 
    for size in range(2, N): # size + 1 means substring length
        foundInThisSize = False
        for i in range(N-size):
            dp[i][i+size] = dp[i+1][i+size-1] and (s[i] == s[i+size])
            if dp[i][i+size] and not foundInThisSize:
                resLeft = i
                resRight = i + size
                foundInThisSize = True

    return s[resLeft : resRight+1]
