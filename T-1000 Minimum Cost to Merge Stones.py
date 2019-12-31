'''
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile,
and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
'''
class Solution:
    '''
    A bottom-up solution
    '''
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1

        # sumArray[i] is the sum of stones[:i]
        # Therefore sum of stones[i:j+1] is sumArray[j+1] - sumArray[i]
        sumArray = [0] * (n+1)
        for i in range(n):
            sumArray[i+1] = sumArray[i] + stones[i]

        # dp[i][j] is the min cost of stone[i:j+1]
        # dp[i][i] should always be 0
        dp = [[0] * n for _ in range(n)]
        
        # The building dp order:
        # [0,2], [1,3], ... [n-2, n]
        # [0,3], [1,4], ... [n-3, n]
        # Same like Burst Balloon problem
        for step in range(K, n+1):
            for left in range(n-step+1):

                # left and right indexes are inclusive
                right  = left + step - 1

                dp[left][right] = 1000000
                # Why increase by K - 1 ?
                # For example, if left = 0, first iteration is dp[0][0] + dp[1][right]
                # If increase by 1, second iteration is dp[0][1] + dp[2][right]
                # However, dp[0][1] could be meaningless when K > 2
                for i in range(left,right,K-1):
                    dp[left][right] = min(dp[left][right], dp[left][i]+dp[i+1][right])

                # If stones [left:right+1] can pile to 1 rock
                # Add the sum of [left:right+1] as a base cost
                if (step - 1) % (K - 1) == 0:
                    dp[left][right] += sumArray[right+1] - sumArray[left]

        return dp[0][n-1]

class Solution:
    '''
    A Top-down solution
    '''
    def getSum(self, left: int, right: int):
        '''
        Return sum of stones in [left, right + 1]
        '''
        return self.accu[right+1] - self.accu[left]
        
    def topDown(self, left: int, right: int) -> int:
        '''
        Top down dynamic programming computing in range [left, right + 1]
        So both indexes are inclusive
        '''
        if self.caches[left][right] is not None:
            return self.caches[left][right]
        
        result = 0
        width = right - left + 1
        if width < self.K:
            result = 0
        elif width == self.K:
            result = self.getSum(left, right)
        else:
            result = float('inf')

            # Current result is the combination of 2 children results.
            # i is the break point. Notice its increment is K - 1
            for i in range(left, right, self.K - 1):
                result = min(result, self.topDown(left, i) + self.topDown(i+1, right))

            # If current subarray a form into a stone, add its cost
            if (width - 1) % (self.K - 1) == 0:
                result += self.getSum(left, right)       

        self.caches[left][right] = result
        return result
    
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        
        self.K = K
        
        # Prepare prefix sum query
        accu = [0] * (n+1)
        for i in range(n):
            accu[i+1] = accu[i] + stones[i]
        self.accu = accu
        
        # Prepare top-down dynamic programming caches
        # caches[i][j] is the minimum cost from stone i to stone j inclusively
        self.caches = [[None] * n for _ in range(n)]
        
        return self.topDown(0, n-1)
