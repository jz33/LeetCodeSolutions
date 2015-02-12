#include <stdio.h>
#include <stdlib.h>
/*
60 Permutation Sequence
https://oj.leetcode.com/problems/permutation-sequence/
*/
void dump(int* arr, const int N){
	int i;
	for(i=0;i<N;i++) printf("%d ",arr[i]);
	printf("\n");
}
void swap(int* x, int* y){
    int t = *x;
    *x = *y;
    *y =t;
}
int perm(int N, int R){
	int res,bottom;
	if(R > N || N < 0 || R <0) return -1;
	
	res = 1;
	bottom = N-R;
	while(N > bottom){
		res *= N--;
	}
	return res;
}
/*
T is [0,1,2,...,full-1]
*/
void permutationSequence(int N, int T){
    int full,dividend,divisor,quotient,remainder,i,j;
    int* arr;
    if(N < 0 || T < 0) return;

    full = perm(N,N);
    if(T > full - 1) return;
    
    arr = (int*)malloc(N*sizeof(int));
    for(i=0;i<N;i++) arr[i] = i+1;

    dividend = T;
    for(i=1;i<N;i++){
        divisor = full / perm(N,i);
        quotient = dividend / divisor;
        remainder= dividend % divisor;
        /*
        A swap mechanism to ensure lexicological order
        */
        for(j=1;j<=quotient;j++){
            swap(arr+i-1,arr+i-1+j);
        }
        dividend = remainder;
    }
    
    dump(arr,N);
    free(arr);
}

int main()
{
	int i,N = 4;
	int full = perm(N,N);
	for(i=0;i<full;i++) permutationSequence(N,i);
	return 0;
}