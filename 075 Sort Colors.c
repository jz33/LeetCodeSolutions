#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
75 Sort Colors
https://oj.leetcode.com/problems/sort-colors/
*/
/*
Generate a random interger in [0,limit]
Avoid using previous one
*/
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
//Swap 2 elements of an array
void swap(int* a, int lt, int rt)
{
    int t = a[lt];a[lt] = a[rt];a[rt] = t;
}
//Test result array
void test(int* a, int N)
{
    int i = 0;
	int valid = 1;
    for(;i<N-1 && valid;i++)
         if(a[i]>a[i+1]) valid = 0;
    if(valid){
		printf("Test of array passed!\n");
	} else{
		printf("Failed!\n");
	}
}
//Create a random int array
void creat(int* a, int N, const int limit)
{
    int i = 0;
    for(;i<N;i++) a[i] = randLimit(limit);
}
//Copy a random int array
void copy(int* src, int N, int* tag)
{
    int i = 0;
    for(;i<N;i++) tag[i] = src[i];
}
// print out int array
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}

void color3(int* arr, int lo, int hi){
	int nextRPos = lo;
    int nextBPos = hi;
	int i  = 0;
    while(i <= nextBPos){
        if(arr[i] == 0) swap(arr,i++,nextRPos++);
        else if(arr[i] == 2) swap(arr,i,nextBPos--);
		else i++;
    }
}
// Tester  
int main(int argc, char* argv[])
{
#define N 10

    int i;
    int colors[N];

    /* 
		Test sort 3 colors. Notation:
		R G B
		0 1 2
	*/
	for(i=0;i<N;i++) colors[i] = randLimit(2);
	dump(colors,N);
    color3(colors,0,N-1);
    dump(colors,N);test(colors,N);

    return 0;
}