'''
805. Split Array With Same Average
https://leetcode.com/problems/split-array-with-same-average/

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C,
and B and C are both non-empty.

Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
'''
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        half = total >> 1 
        average = total / len(A)
        
        # Compute all possible sums from [0, half]
        # For each sum, record how many number used
        dp = [{0}] + [set() for _ in range(half)]
        for n in A:
            for i in range(half, n-1, -1):
                if n != 0:
                    for c in dp[i-n]:
                        dp[i].add(c + 1)
                elif dp[i]:
                    # Special case when n == 0
                    mx = max(c for c in dp[i])
                    dp[i].add(mx + 1)
        
        # Try all partitions
        for cut in range(1, len(A) // 2 + 1):
            subTotal = float(cut) * average       
            
            # Need to round the float to make less accurate
            if round(subTotal, 5).is_integer():          
                si = int(round(subTotal))           
                if cut in dp[si]:
                    return True
                
        return False
