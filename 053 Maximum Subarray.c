/*
Maximum Subarray
https://oj.leetcode.com/problems/maximum-subarray/

Kadane’s Algorithm for 
largest sum of a contiguous array
*/
int MaxSubArrSum(int* arr, const int N){
    int max_so_far = 0, max_ending_here = 0;
    int i;
    for(i = 0;i<N;i++)
    {
        max_ending_here += arr[i];
        if(max_ending_here < 0) 
            max_ending_here = 0;
        else if(max_so_far < max_ending_here)
            max_so_far = max_ending_here;
    }
    return max_so_far;
}  

int main()
{
    //TODO: test
    return 0;
}