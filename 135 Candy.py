'''
135. Candy
https://leetcode.com/problems/candy/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]: # and candies[i] <= candies[i-1]
                candies[i] = candies[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1;

        return sum(candies)
