#include <stdio.h>
#include <stdlib.h>
/*
205 Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find Kth Largest / Smallest Element in an Array
*/
#define ARRAY_SIZE(a,t) (sizeof(a)/sizeof(t))

int randLimit(const int limit)
{
	static int prev;
    int div = RAND_MAX/(limit+1);
    int res = -1;
    do{ 
        res = rand() / div;
    }while (res > limit || res == prev);
	prev = res;
    return res;
}
void swap(int* a, int* b)
{
    int t = *a;*a = *b;*b = t;
}
// print out int array
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
/*
"return x - y" : kth largest
"return y - x" : kth smallest
*/
int comp(int x, int y)
{
    return x - y;
}
/*
A standard partition method
*/
int partition(int* a, int lt, int rt)
{
    int pivot = randLimit(rt-lt)+lt;
    int pval = a[pivot];
    int new_pivot = lt;
    int i = lt;
    
    swap(a + rt, a + pivot); //Put a[pivot] to right
    for (;i<rt;i++)
        // if $comp > 0, move current to left
        if(comp(a[i],pval)>0) {
            swap(a + i, a + new_pivot);
            new_pivot++;
        }
    swap(a + rt, a + new_pivot);
    return new_pivot;
}
/*
Not used here
*/
void quicksort(int* a, int lt, int rt)
{
    int pivot = -1;
    if(lt>=rt) return;
    pivot = partition(a, lt, rt);
    quicksort(a, lt, pivot-1);
    quicksort(a, pivot+1, rt);
}
/*
Quick select
avg O(n), worst O(n^2)
*/
int quickselect(int* a, int lt, int rt, int tag)
{
    int pivot;
    if(lt>=rt) return a[lt]; 
    pivot = partition(a, lt, rt);
    if(pivot == tag) return a[tag];
    else if(pivot > tag) return quickselect(a, lt, pivot-1, tag);
    else return quickselect(a, pivot+1, rt, tag);
}
/*
How to use
*/
int findKthLargest(int* nums, int numsSize, int k) {
    return quickselect(nums,0,numsSize-1,k-1);
}
/*
Given [3,2,1,5,6,4] and k = 2, return 5.
*/
int main()
{
    int arr[] = {3,2,1,5,6,4};
    int tag = 2,r;
    
    dump(arr,ARRAY_SIZE(arr,int));
    
    // notice minus 1
    r = quickselect(arr,0,sizeof(arr)/sizeof(int)-1,tag-1);
    printf("%d\n",r);
    
    quicksort(arr,0,ARRAY_SIZE(arr,int)-1);
    dump(arr,ARRAY_SIZE(arr,int));
    
    return 0;
}
