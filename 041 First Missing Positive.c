#include <stdio.h>
#include <stdlib.h>
/*
First Missing Positive
https://oj.leetcode.com/problems/first-missing-positive/
http://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
*/
void swap(int* i,int* j){
    int t = *i;
    *i    = *j;
    *j    = t;
}
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
int firstMissingPositive(int arr[], int size)
{
    int i,j,k;
    
    // 1. move all negative or 0 numbers to right
	// 2 colors problem
    i = 0;
    j = size-1;
    while(i<j){
        while(i<=j && arr[i] > 0) i++;
        while(i<=j && arr[j] <=0) j--;
        if(i<j) swap(arr+i,arr+j);
    }
    
    // all negative or 0
    if(j==-1) return 1; 
    dump(arr,size); // debug

    // 2. assign negative if visited
    for(i = 0;i<=j;i++){
		k = abs(arr[i]);
        if(k<=j){
            if(arr[k]>0){
                arr[k] = -arr[k];
				dump(arr,size); // debug
			}
		}
    }
    
    // 3. find first non-negative, skip 0
    for(i = 1;i<=j;i++) if(arr[i]>0) return i;
    
    // all negative, notice the first element
	// e.g., int arr[] = {0,-10,1,-5,0,2,3,4};
    return j+1 == arr[0] ? arr[0]+1 : j+1;
}
/*
Tester
*/
int main()
{
    //int arr[] = {0,5,-2,3,7,1,2,-15};
	//int arr[] = {0,-10,1,-5,0,2,3,4};
	int arr[] = {0,1,1,1,1,1,1};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    printf("%d\n", firstMissingPositive(arr, arr_size));
    return 0;
}