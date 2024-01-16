'''
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
    0 <= num <= 108
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))
        maxIndex = len(numList) - 1 # the index that has the maximum value
        swapLeft, swapRight = None, None # swap candidates

        # From right to left, find the swap indexes.
        # The value of left swap index must be smaller than value on max index,
        # and the left swap index should be as left as possible
        for i in range(len(numList)-1, -1, -1):
            if numList[i] > numList[maxIndex]:
                maxIndex = i
            elif numList[i] < numList[maxIndex]:
                swapLeft = i
                swapRight = maxIndex
        
        if swapLeft is not None:
            numList[swapLeft], numList[swapRight] = numList[swapRight], numList[swapLeft]
            return int(''.join(numList))
        else:
            # If swapLeft is None, the num is already the largest
            return num
