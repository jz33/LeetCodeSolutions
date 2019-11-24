/*
325. Maximum Size Subarray Sum Equals k
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/submissions/

Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
*/
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        // The map stores {sum : leftmost index}
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        map.put(0,-1);

        int accu = 0;
        int maxlen = 0;
        for (int i = 0;i<nums.length;i++) {
            accu += nums[i];
            maxlen = Math.max(maxlen, i - map.getOrDefault(accu - k,i));
            map.putIfAbsent(accu,i);
        }
        return maxlen;
    }
}
