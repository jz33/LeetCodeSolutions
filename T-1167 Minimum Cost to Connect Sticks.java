/*
1167. Minimum Cost to Connect Sticks
https://leetcode.com/problems/minimum-cost-to-connect-sticks/

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:

Input: sticks = [2,4,3]
Output: 14

Example 2:

Input: sticks = [1,8,3,5]
Output: 30

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
*/
import java.util.*;

class Solution {
    public int connectSticks(int[] sticks) {
        int size = sticks.length;
        PriorityQueue<Integer> queue = new PriorityQueue<>(sticks.length);
        for (int i = 0; i < size; ++i) {
            queue.offer(sticks[i]);
        }
        
        int minCost = 0;
        while (queue.size() > 1) {
            int cost = queue.poll() + queue.poll();
            minCost += cost;
            queue.offer(cost); // cost is like a new stick
        }

        return minCost;
    }
}
