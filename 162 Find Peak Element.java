/**
 * Find Peak Element
 * https://leetcode.com/problems/find-peak-element/
 * This approach assumes peak exists
 */
public int findPeakElement(int[] nums)
{
    int lt = 0;
    int rt = nums.length - 1;
    int mid = 0;
    while(lt <= rt)
    {
        if(lt == rt)
            return lt;
        if(lt + 1 == rt)
            return nums[lt] > nums[rt] ? lt:rt;
            
        mid = (lt+rt)>> 1;
        if(nums[mid - 1] < nums[mid] && nums[mid + 1] < nums[mid])
        {
            return mid;
        }
        if(nums[mid - 1] < nums[mid])
        {
            lt = mid + 1;
        }
        else
        {
            rt = mid - 1;
        }
    }
    return -1;
}
