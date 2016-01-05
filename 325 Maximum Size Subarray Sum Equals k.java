import java.util.*;
/*
325 Maximum Size Subarray Sum Equals k
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
*/
public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        // sum : leftmost index
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        map.put(0,-1);
        int length = nums.length;
        int accu = 0;
        int maxlen = 0;
        for(int i = 0;i<length;i++){
            accu += nums[i];
            maxlen = Math.max(maxlen, i - map.getOrDefault(accu - k,i));
            map.putIfAbsent(accu,i);
        }
        return maxlen;
    }
}
