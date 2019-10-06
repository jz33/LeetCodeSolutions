'''
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
'''
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        size = len(A)
        if size < 2:
            return True
        
        UP = 1
        DOWN = 2
        
        tone = None
        for i in range(1, size):
            curr = A[i]
            prev = A[i-1]
            if curr > prev:
                if not tone:
                    tone = UP
                elif tone == DOWN:
                    return False
            elif curr < prev:
                if not tone:
                    tone = DOWN
                elif tone == UP:
                    return False
            
        return True
