'''
801. Minimum Swaps To Make Sequences Increasing
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
'''
# Since the question guarantees there is a solution,
        # then we only care about costs
        n = 0 # the minimun cost if column i is not swapped
        s = 1 # the minimun cost if column i is swapped
        
        for i in range(1, len(A)):
            ni = float('inf')
            si = float('inf')
            
            if A[i-1] < A[i] and B[i-1] < B[i]:
                ni = n # i-1, i both not swap
                si = s + 1 # i-1, i both swap
                
            if A[i-1] < B[i] and B[i-1] < A[i]:
                ni = min(ni, s) # only swap i-1
                si = min(si, n + 1) # only swap i
                
            # At least one of above should be hit.
            # Other cases we cannot swap either i-1 or i
            
            n = ni
            s = si

        return min(n, s)
