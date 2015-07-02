#include <stdio.h>
/*
Search in Rotated Sorted Array
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
*/
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
/*
A normal binary search for sorted array
*/
void binary(int* arr, int L, int R, const int tag, int* res)
{
    int mid;
    *res = -1;
    while(L <= R)
    {
        mid = (L+R) >> 1;
        if(arr[mid] == tag){
            *res = mid;
            break;
        } else if(arr[mid] < tag){
            L = mid+1;
        } else {
            R = mid-1;
        }
    }
}
/*
An iterative approach by finding the "bend point" first
*/
#define DEBUG 1
int search(int* arr, const int N, const int tag)
{
    int res, leftmost, rightmost, lt, rt, mid, bendInd;
    if(N == 0) return -1;
    if(N == 1) return arr[0]==tag ? 0:-1;
    
    res = -1;
    leftmost = arr[0];
    rightmost= arr[N-1];
    
    if(leftmost < rightmost)
    {
        // normal binary search
        binary(arr,0,N-1,tag, &res);
        return res;
    }
    
    // fine "bend point"
    lt = 0;
    rt = N-1;
    bendInd = -1;
    while(lt <= rt)
    {
        mid = (lt+rt) >> 1;
        if((mid - 1 > -1 && arr[mid - 1] <= arr[mid]) &&
           (mid + 1 < N  && arr[mid + 1] <  arr[mid])
        ){
            bendInd = mid;
            break;
        } 
        else if(arr[mid] >= leftmost)
            lt = mid+1;
        else // arr[mid] <= rightmost
            rt = mid-1;
    }
    // if not found, assign lt as bend point
    if(bendInd == -1) bendInd = 0; if(DEBUG) printf("bend: %d\n",bendInd);
    
    // search
    if(
        (tag > arr[bendInd]) ||
        (tag < arr[bendInd + 1]) ||
        (tag < leftmost && tag > rightmost)
    ) return res;
    
    if(tag <= arr[bendInd] && tag >= leftmost)
    {
        if(DEBUG) printf("left\n");
        binary(arr,0,bendInd,tag,&res);
    }
    else
    {
        if(DEBUG) printf("right\n");
        binary(arr,bendInd+1,N-1,tag,&res);
    }
    return res;
}
/*
Tester
*/
void test_iterative(void)
{
    int arr[] = {4,5,1,2,3};
    int size = sizeof(arr)/sizeof(int);
    int tag = 1;
    
    printf("%d\n",search(arr,size,tag));
}
int main(int argc, char* argv[])
{
    test_iterative();
    return 0;
}
