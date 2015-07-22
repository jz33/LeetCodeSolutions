#include <stdio.h>
/*
Search in Rotated Sorted Array
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
*/
int search(int* arr, int size, int tag)
{
    int lt,rt,mid,rightmost;

    lt = 0;
    rt = size - 1;
    rightmost = arr[rt];

    while(lt <= rt)
    {  
        mid = (lt + rt) >> 1;
        if(tag == arr[mid])
            return mid;
       
        /*
        Notice the reason to use right most rather than
        left most. The array can have no turn.
        */
        if(tag > rightmost)
        {
            if(tag > arr[mid] && arr[mid] > rightmost)
                lt = mid + 1;
            else 
                rt = mid - 1;
        }
        else
        {   
            if(tag < arr[mid] && arr[mid] < rightmost )
                rt = mid - 1;
            else 
                lt = mid + 1;
        }
    }
    return -1;
}
