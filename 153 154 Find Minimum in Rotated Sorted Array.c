#include <stdio.h>
/*
153 Find Minimum in Rotated Sorted Array
154 Find Minimum in Rotated Sorted Array II
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Simpler than "Search in Rotated Sorted Array"
Below method makes same result on duplicated or duplicatedless array
*/
#define MIN(a,b) (a)<(b)?(a):(b)
void dump(int* arr, const int arrSize)
{
    int i = 0;
    for(;i<arrSize;i++) printf("%d ",arr[i]);
    printf("\n");
}
/*
Assume "arr" has only positive elements
*/
void search(int* arr, int L, int R, int* res)
{
    int mid, leftmost, rightmost;
    if(L>R || *res != -1) return;
    if(L == R){
        *res = arr[L];
        return;
    }
    if(L+1 == R){
        *res = MIN(arr[L],arr[R]);
        return;
    }
    
    leftmost = arr[L];
    rightmost= arr[R];
    mid = (L+R)>>1;
    
    if(leftmost <= rightmost){
        // normal binary search
        *res = leftmost;
    } else {
        // do not forget "mid" !
        if(arr[mid] >= leftmost) search(arr,mid,R,res);
        else if(arr[mid] <= rightmost) search(arr,L,mid,res); 
    }
}
/*
Tester
*/
int main(int argc, char* argv[])
{
#define N 15

    int t0[N];// No duplicates
	int t1[N];// Duplicated
    int i,cut;
    int res = -1;
    
    for(i=0;i<N;i++) t0[i] = i;
    dump(t0,N);
    search(t0,0,N-1,&res);
    printf("Search for normal sorted array: %d\n",res);

    printf("Search for rotated sorted array (NO duplicates):\n");
    cut = 6;
    for(i=cut;i<N;i++) t0[i] = i;
    for(i=0;i<cut;i++) t0[i] = i+N;
    dump(t0,N);

    res = -1;
    search(t0,0,N-1,&res);
	printf("%d\n",res);

    printf("Search for rotated sorted array (Duplicated):\n");
	cut = 6;
    for(i=cut;i<N;i++) t1[i] = i + i%2;
    for(i=0;i<cut;i++) t1[i] = i+N + i%2;
    dump(t1,N);

    res = -1;
    search(t0,0,N-1,&res);
    printf("%d\n",res);

    return 0;
}
