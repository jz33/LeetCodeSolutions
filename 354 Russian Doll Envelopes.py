'''
354. Russian Doll Envelopes
https://leetcode.com/problems/russian-doll-envelopes/

You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than
the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''
def searchInsert(arr: List[int], tag: int) -> int:
    left = 0
    right = len(arr) - 1       
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] == tag:
            return mid
        elif arr[mid] < tag:
            left = mid + 1
        else:
            right = mid - 1      
    return left
    
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by env[0] ascending and env[1] descending, 
        # and this problem reduces to Longest Increasing Subsequence problem
        # Why ascending then descending? Think example like [5, 8], [5, 10]
        # If consider [5, 8] first, 8 is added; when considering [5, 10]
        # 10 will be added after 8, but [5, 10]  cannot cover [5, 8] 
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        # arr is ascendingly sorted by env[1]
        arr = []
        for env in envelopes:
            tag = env[1]
            ip = searchInsert(arr, tag)

            if ip >= len(arr):
                arr.append(tag)
            else:
                arr[ip] = tag

        return len(arr)
        
# More examples
ls = [[5,4],[6,4],[6,7],[2,3]] # 3
ls = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]] # 5
ls = [[46,89],[50,53],[52,68],[72,45],[77,81]] # 3
ls = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]] # 5

sol = Solution()
print(sol.maxEnvelopes(ls))
