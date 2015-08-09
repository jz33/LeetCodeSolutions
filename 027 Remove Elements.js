var removeElement = function(nums, val)
{
    var i = 0;
    for(;i < nums.length;i++)
    {
        if(nums[i] != val)
            break;
    }

    var j = 0;
    for(;i < nums.length;i++)
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
