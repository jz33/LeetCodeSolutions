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

// Tester  
int main(int argc, char* argv[])
{
#define N 15

    const int limit = 4;
    int ori[N];
    int t0[N];
    int i,lt,rt;
    int tag = 0;
    
    creat(ori,N,limit);
    dump(ori,N);
    
    // test quick sort
    copy(ori,N,t0);
    qsort(t0,N,sizeof(int),compInt);
    dump(t0,N);
    
    search(t0,N,tag,&lt,&rt);
    printf("Search for tag: %d, in range: [%d,%d]\n",tag,lt,rt);
    
    return 0;
}
