/*
Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/
/*
Kadane’s Algorithm
Assume $size >= 1
And notice $global CANNOT start from 0
*/
int kadaneMax(int* arr, int size)
{
    int local, global, i;
    if(size == 0) return -1;

    local = arr[0];
    global = local;

    for(i = 1;i<size;i++)
    {
        if(local < 0) local = 0;
        
        local += arr[i];
        if(global < local) global = local;
    }
    return global;
}  
int kadaneMin(int* arr, int size)
{
    int local, global, i;
    if(size == 0) return -1;

    local = arr[0];
    global = local;

    for(i = 1;i<size;i++)
    {
        if(local > 0) local = 0;
        
        local += arr[i];
        if(global > local) global = local;
    }
    return global;
}
