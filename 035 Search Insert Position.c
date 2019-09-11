/*
Search Insert Position
https://oj.leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
*/
#include <stdio.h>

void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}

// A normal recursive approach
void binary(int* arr, int L, int R, const int tag, int* res)
{
    int mid;
    if(L>R) return;
    
    mid = (L+R) >> 1;
    if(arr[mid] == tag){
        *res = mid;
        return;
    }
    
    // L = R-1 or L == R
    if(mid == L){
        if(tag < arr[L]) *res = L;
        else if (tag > arr[L] && tag <= arr[R]) *res = L+1;
		else *res = R+1; // (tag >= arr[R])
        return;
    }

    if(arr[mid] < tag){
        binary(arr,mid+1,R,tag,res);
    } else {
        binary(arr,L,mid-1,tag,res);
    }
}
int recursiveSearch(int* arr, const int N, const int tag)
{
    int res = -1;
    binary(arr,0,N-1,tag,&res);
    return res;
}

// an iterative approach
int iterativeSearch(int* arr, const int N, const int tag)
{
    int i = 0;
    int j = N - 1;
    int mid;

    while(i<=j)
    {
        mid = (i+j) >> 1;
        if(arr[mid] == tag) return mid;
        
        // i = j-1 or i == j
        if(mid == i){
            if(tag < arr[i]) return i;
            else if (tag > arr[i] && tag <= arr[j]) return i+1;
            else // (tag > arr[R])
                return j+1;
        }
        if(arr[mid] < tag) i = mid + 1;
        else j = mid - 1;
    }
    return -1;
}

// Tester  
int main(int argc, char* argv[])
{
#define N 4

    int t0[N];
    int i;
    
    t0[0] = 1;t0[1]=3;t0[2]=5;t0[3]=6;
    dump(t0,N);
    
    printf("Search for value %d: %d\n",5,recursiveSearch(t0,N,5));
    printf("Search for value %d: %d\n",2,recursiveSearch(t0,N,2));
	printf("Search for value %d: %d\n",7,recursiveSearch(t0,N,7));
	printf("Search for value %d: %d\n",0,recursiveSearch(t0,N,0));
    
    printf("Search for value %d: %d\n",5,iterativeSearch(t0,N,5));
    printf("Search for value %d: %d\n",2,iterativeSearch(t0,N,2));
	printf("Search for value %d: %d\n",7,iterativeSearch(t0,N,7));
	printf("Search for value %d: %d\n",0,iterativeSearch(t0,N,0));
    return 0;
}
