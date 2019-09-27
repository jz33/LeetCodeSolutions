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
class Solution:
    def getInsertionPoint(self, arr: List[int], tag: int, left: int, right: int) -> int:
        '''
        Find insertion point of tag in arr, arr is ascendingly sorted.
        '''
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid] == tag:
                return mid

            if mid == left:
                # left = right - 1 or left == right
                if tag < arr[left]:
                    return left;
                elif tag > arr[left] and tag <= arr[right]:
                    return right;
                else: # tag > arr[right]
                    return right + 1;

            if arr[mid] < tag:
                left = mid + 1
            else:
                right = mid - 1

        return 0 # Reachable when len(arr) = 0
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by env[0] ascending and env[1] DESCENDING
        # And this problem reduces to Longest Increasing Subsequence problem
        # Why DESCENDING? Think example like [5, 8], [5, 10]
        # If consider [5, 8] first, 8 is added; when considering [5, 10]
        # 10 will be added after 8, but [5, 10]  cannot cover [5, 8] 
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        # graph is ascendingly sorted env[1]
        graph = []
        for env in envelopes:
            tag = env[1]
            ip = self.getInsertionPoint(graph, tag, 0, len(graph)-1);

            if ip > len(graph)-1:
                graph.append(tag)
            else:
                graph[ip] = tag

        return len(graph)
        
# More examples
ls = [[5,4],[6,4],[6,7],[2,3]] # 3
ls = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]] # 5
ls = [[46,89],[50,53],[52,68],[72,45],[77,81]] # 3
ls = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]] # 5

sol = Solution()
print(sol.maxEnvelopes(ls))
