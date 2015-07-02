#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
Search for a Range
https://oj.leetcode.com/problems/search-for-a-range/
*/
int randLimit(const int limit)
{
    int div = RAND_MAX/(limit+1);
    int res = -1;
    do{ 
        res = rand() / div;
    }while (res > limit);
    return res;
}
void creat(int* a, int N, const int limit)
{
    int i = 0;
    for(;i<N;i++) a[i] = randLimit(limit);
}
void copy(int* src, int N, int* tag)
{
    int i = 0;
    for(;i<N;i++) tag[i] = src[i];
}
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
int compInt(const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
/*
Old recursive approach
*/
void searchRec(int* arr, int L, int R, const int N, const int tag, int* lt, int* rt)
{
    int mid = (L+R) >> 1;
    
    if(L>R) return;
    if(arr[mid] == tag){
        *lt = mid;
        while(*lt-1 > -1 && arr[*lt-1] == tag) *lt = *lt - 1;
        *rt = mid;
        while(*rt+1 < N  && arr[*rt+1] == tag) *rt = *rt + 1;
    } else if(arr[mid] < tag){
        searchRec(arr,mid+1,R,N,tag,lt,rt);
    } else {
        searchRec(arr,L,mid-1,N,tag,lt,rt);
    }
}
void search(int* arr, const int N, const int tag, int* lt, int* rt)
{
    *lt = -1;
    *rt = N-1;
    searchRec(arr,0,N-1,N,tag,lt,rt);
}
/*
Iterative approach
*/
int* searchRange(int* arr, int size, int tag, int* returnSize)
{
    int* range;
    int mid, lt, rt;
    
    *returnSize = 2;
    range = (int*)malloc(sizeof(int)*(*returnSize));
    range[0] = -1; range[1] = -1;
    if(size < 1) return range;
    
    lt = 0;
    rt = size - 1;
    while(lt <= rt)
    {
        mid = (lt+rt) >> 1;
        if(arr[mid] == tag)
        {
            range[0] = mid;
            while(range[0] - 1 > -1 && arr[range[0] - 1] == tag) range[0] -= 1;
            range[1] = mid;
            while(range[1] + 1 < size && arr[range[1] + 1] == tag) range[1] += 1;
            return range;
        }
        else if(arr[mid] < tag)
            lt = mid + 1;
        else
            rt = mid - 1;
    }
    return range;
}
// Tester  
int main(int argc, char* argv[])
{
#define N 15

    const int limit = 4;
    int ori[N];
    int t0[N];
    int i,lt,rt;
    int tag = 0;
    
    int returnSize = 2;
    int* iter;
    
    creat(ori,N,limit);
    dump(ori,N);
    
    // test quick sort
    copy(ori,N,t0);
    qsort(t0,N,sizeof(int),compInt);
    dump(t0,N);
    
    search(t0,N,tag,&lt,&rt);
    printf("Search for tag: %d, in range: [%d,%d]\n",tag,lt,rt);
    
    iter = searchRange(t0, N, tag, &returnSize);
    printf("Iterative: [%d,%d]\n",iter[0],iter[1]);
    
    free(iter);
    return 0;
}
