#include <stdio.h>
#include <stdbool.h>
/*
Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
*/
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
bool search(int* arr, int size, int tag)
{
    int lt,rt,mid;
    lt = 0;
    rt = size - 1;
    
    while(lt <= rt)
    {
        mid = (lt + rt) >> 1;
        if(arr[mid] == tag) return true;

        while(arr[lt] == arr[mid] && arr[rt] == arr[mid])
        {
            lt++; 
            rt--;
        }
        
        if(arr[lt] <= arr[mid])
        {
            if(tag >= arr[lt] && tag < arr[mid]) 
                rt = mid - 1;
            else 
                lt = mid + 1; 
        }
        else
        {  
            if(tag > arr[mid] && tag <= arr[rt]) 
                lt = mid + 1;
            else 
                rt = mid - 1;
        }
    }
    return false;
}
/*
Tester
*/
void test_iterative(void)
{
    int arr[] = {1,3,5};
    int size = sizeof(arr)/sizeof(int);
    int tag = 1;
    
    printf("%u\n",search(arr,size,tag));
}
int main(int argc, char* argv[])
{
    test_iterative();
    return 0;
}
