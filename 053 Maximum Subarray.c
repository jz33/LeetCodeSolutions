/*
Maximum Subarray
https://oj.leetcode.com/problems/maximum-subarray/
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
int main()
{
    //TODO: test
    return 0;
}
