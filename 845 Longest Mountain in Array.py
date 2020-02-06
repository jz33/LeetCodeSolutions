'''
845. Longest Mountain in Array
https://leetcode.com/problems/longest-mountain-in-array/

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0
        
        # 0: flat
        # 1: ascending
        # 2: descending        
        direction = 0 
        maxLength, localLength = 0, 1

        def update():
            nonlocal maxLength, localLength
            if direction == 2:
                maxLength = max(maxLength, localLength)
                localLength = 1 
        
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                update()
                direction = 0
                localLength = 1
                
            elif A[i] > A[i-1]:
                update()
                direction = 1
                localLength += 1
                
            else:
                if direction == 0:
                    localLength = 1
                else:
                    direction = 2
                    localLength += 1
        
        update()
        return maxLength
