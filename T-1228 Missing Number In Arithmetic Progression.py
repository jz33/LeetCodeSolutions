'''
1228. Missing Number In Arithmetic Progression
https://leetcode.com/problems/missing-number-in-arithmetic-progression/

In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are
all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.

Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].

Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
'''
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        gap, gapStart = None, None
        for i in range(1, len(arr)):
            g = arr[i] - arr[i-1]
            if gap is None:
                gap = g
                gapStart = arr[i-1]
            elif g == gap * 2:
                return arr[i-1] + gap
            elif g * 2 == gap:
                return gapStart + g
        return -1
