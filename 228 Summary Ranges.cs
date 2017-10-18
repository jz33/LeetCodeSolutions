/*
228 Summary Ranges
https://leetcode.com/problems/summary-ranges
*/
using System.Text;

public class Solution {
    private string GetRange(int[] nums, int left, int right){
        var ss = new StringBuilder(nums[left].ToString());
        if (right - 1 != left)
        {
            ss.Append("->");
            ss.Append(nums[right-1]);
        }
        return ss.ToString();
    }
    public IList<string> SummaryRanges(int[] nums) {
        var res = new List<string>();
        if (nums == null || nums.Length < 1) return res;
        int left = 0;
        int right = 1;
        for(;right<nums.Length;right++){
            if(nums[right] - 1 != nums[right-1])
            {
                res.Add(GetRange(nums,left,right));
                left = right;
            }
        }
        res.Add(GetRange(nums,left,right));
        return res;
    }
}
