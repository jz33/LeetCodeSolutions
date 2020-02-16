'''
862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
 
Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1

Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
'''
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        res = -1
        
        # Build prefix sum array
        prefixSum = [0] * (len(A)+1)
        for i in range(len(A)):
            prefixSum[i+1] = prefixSum[i] + A[i]
        
        # Queue contains the index of prefixSum, for all i
        # in queue, prefixSum[i] is ascending
        queue = collections.deque()
        for i, s in enumerate(prefixSum):
            while queue and s <= prefixSum[queue[-1]]:
                queue.pop()
                
            # Try update result using queue[0], as
            # queue[0] and i can compose the subarray with largest sum.
            # If even that sum is smaller than K, no more element later
            # in queue will meet the requirement of >= K
            while queue and s - prefixSum[queue[0]] >= K:
                j = queue.popleft()
                if res == -1 or i - j < res:
                    res = i - j
            
            queue.append(i)
            
        return res
