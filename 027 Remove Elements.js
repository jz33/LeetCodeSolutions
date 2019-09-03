/**
 * Remove Element
 * https://leetcode.com/problems/remove-element/
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val)
{
    var j = 0; // return length
    for(var i = 0; i < nums.length; i++)
    {
        if(nums[i] != val)
        {
            nums[j] = nums[i];
            j++;
        }
    }

    nums.length = j;
    return j;
};
