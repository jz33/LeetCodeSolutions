'''
1231. Divide Chocolate
https://leetcode.com/problems/divide-chocolate/

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts,
each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
'''
class Solution:
    def getPiecesCount(self, sweetness: List[int], total: int) -> int:
        '''
        Get count of subarrays whose sum is >= total
        '''
        count = 0
        prefixSum = 0
        for sweet in sweetness:
            prefixSum += sweet
            if prefixSum >= total:
                count += 1
                prefixSum = 0
        return count
            
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        size = len(sweetness)        
        left = min(sweetness) 
        right = sum(sweetness)
        maxSweet = left
        
        while left <= right:
            mid = left + ((right - left) >> 1);
            count = self.getPiecesCount(sweetness, mid)

            if count >= K+1:
                maxSweet = max(maxSweet, mid)
                left = mid + 1
            else:
                right = mid - 1

        return maxSweet
