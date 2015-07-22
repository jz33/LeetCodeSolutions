#include <stdio.h>
/*
153 Find Minimum in Rotated Sorted Array
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/
*/
#define MIN(a,b) (a)<(b)?(a):(b)
int search(int* arr, int size)
{
    int lt,rt,mid,rightmost;

    lt = 0;
    rt = size - 1;
    rightmost = arr[rt];

    while(lt <= rt)
    {
        if(lt == rt)
            return arr[lt];
        if(lt + 1 == rt)
            return MIN(arr[lt],arr[rt]);
            
        mid = (lt + rt) >> 1;
        if(arr[mid-1] > arr[mid])
            return arr[mid];
       
        /*
        Notice the reason to use right most rather than
        left most. The array can have no turn.
        */
        if(arr[mid] > rightmost)
        {
            lt = mid + 1; 
        }
        else
        {   
            rt = mid - 1;
        }
    }
}
int main()
{
    int arr[] = {3,1,1};
    int arr[] = {1,1,3};
    int r = search(arr,sizeof(arr)/sizeof(int));
    printf("%d\n",r);
    return 0;
}
