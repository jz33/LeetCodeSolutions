'''
2055. Plates Between Candles
https://leetcode.com/problems/plates-between-candles/

There is a long table with a line of plates and candles arranged on top of it.
You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive).
For each query, you need to find the number of plates between candles that are in the substring.
A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|".
The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.


Example 1:

Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:

Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

Constraints:
    3 <= s.length <= 105
    s consists of '*' and '|' characters.
    1 <= queries.length <= 105
    queries[i].length == 2
    0 <= lefti <= righti < s.length
'''
'''
Copied from 35
'''
def getInsertionPoint(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        midVal = nums[mid]
        if midVal == target:
            return mid
        if midVal < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # build indexes of candles for binary search
        candles = [i for i, e in enumerate(s) if e == '|'] 

        def getCandleCount(leftQuery: int, rightQuery: int) -> int:
            left = getInsertionPoint(candles, leftQuery)
            # If not found exact match for left query, use the insertion point (if in bound)
            if left >= len(candles):
                return 0
            
            # If not found exact match for right query, use the insertion point - 1 (if in bound) 
            right = getInsertionPoint(candles, rightQuery)
            if right >= len(candles) or rightQuery != candles[right]:
                right -= 1
            if right < 0:
                return 0
            
            # Less than 2 candles
            if left >= right:
                return 0
            
            totalObjects = candles[right] - candles[left] + 1
            candlesCount = right - left + 1
            return totalObjects - candlesCount   
            
        return [getCandleCount(left, right) for left, right in queries]
