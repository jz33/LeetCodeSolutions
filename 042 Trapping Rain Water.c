#include <stdio.h>
#include <stdlib.h>
/*
Trapping Rain Water
https://oj.leetcode.com/problems/trapping-rain-water/
http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
*/
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

int trap(int A[], int n)
{
    int *l,*r, t, i,water;
    if (n<2) return 0; 
     
    l = (int*)malloc(sizeof(int)*n);
    r = (int*)malloc(sizeof(int)*n);
    
    l[0]=0;
    for(i=1;i < n;i++){
        l[i] = MAX(A[i-1],l[i-1]);
    }
    
    r[n-1] = 0;
    for(i = n-2;i > -1;i--){
        r[i] = MAX(A[i+1],r[i+1]);
    }
    
    water = 0;
    for(i=1;i < n-1;i++){
        t = MIN(l[i],r[i]);
        t -= A[i];
        water += MAX(t,0);
    }  
    free(l);
    free(r);
    return water;
}
/*
Tester
*/
int main()
{
	int arr[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    printf("%d\n", trap(arr, arr_size));
    return 0;
}