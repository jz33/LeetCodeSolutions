#include <stdio.h>
#include <stdlib.h>
/*
First Missing Positive
*/
#define DEBUG 1

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
int firstMissingPositive(int* arr, int size)
{
    int i,j,k;
    
    // 1. Move all negative numbers to right
    i = 0;
    j = size-1;
    while(i<=j){
        while(i<=j && arr[i] >= 0) i++;
        while(i<=j && arr[j] <  0) j--;
        if(i<j) swap(arr+i,arr+j);
    }
    
    // All negative or 0, $i never moved, $j is at front
    if(i == 0 && j == -1) return 1; 
    if(DEBUG){
        printf("First: ");
        dump(arr,size);
        printf("i: %d, j: %d\n",i,j);
    }
        
    // 2. Assign arr[k-1] to negative if visited
    for(i = 0;i<=j;i++){
		k = abs(arr[i]);
        if(k <= size && k > 0) // ignore k == 0
        {
            if(arr[k-1] > 0) arr[k-1] = -arr[k-1];
            else if(arr[k-1] == 0) arr[k-1] = -(size+1);
        }
		
		if(DEBUG){
		    printf("k : %d\n",k);
		    dump(arr,size);
		}
    }
    
    // 3. Find first non-negative
    for(i = 0;i<=j;i++)
        if(arr[i]>=0)
            return i+1;
    
    return j+2;
}
/*
Tester
*/
int main()
{
    //int arr[] = {0,5,-2,3,7,1,2,-15};
    //int arr[] = {0,-10,1,-5,0,2,3,4};
    //int arr[] = {1,2,0}; // 3
    //int arr[] = {1}; // 2
    //int arr[] = {1,2,3}; // 4
    //int arr[] = {0}; // 1
    //int arr[] = {2,2}; // 1
    //int arr[] = {-10,-3,-100,-1000,-239,1};
    int arr[] = {1,0,3,3,0,2};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    printf("%d\n", firstMissingPositive(arr, arr_size));
    return 0;
}
