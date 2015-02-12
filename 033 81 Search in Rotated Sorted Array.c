#include <stdio.h>
/*
33 Search in Rotated Sorted Array
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
81 Search in Rotated Sorted Array II
https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/

If array has duplicates, below method will return one of 
the indexes
*/
void dump(int* a, int N)
{
    int i = 0;
    for(;i<N;i++) printf("%d ",a[i]);
    printf("\n");
}
/*
A normal binary search for sorted array
*/
void binary(int* arr, int L, int R, const int tag, int* res)
{
    int mid;
    while(L <= R)
    {
        mid = (L+R) >> 1;
        if(arr[mid] == tag){
            *res = mid;
            break;
        } else if(arr[mid] < tag){
            L = mid+1;
        } else {
            R = mid-1;
        }
    }
}
/*
*/
void rotated(int* arr, int L, int R, const int tag, int leftmost, int rightmost, int goleft, int* res){
    int mid;
    if(L>R) return;
    
    mid = (L+R) >> 1;
    if(arr[mid] == tag){
        *res = mid;
        return;
    }
    
    // L = R-1 or L == R
    if(mid == L){
        *res = arr[R] == tag ? R : -1;
        return;
    }
    
    if(goleft == 1){ // result sits in left side
        if(arr[mid] <= rightmost){
            rotated(arr,L,mid-1,tag,leftmost,arr[mid-1],goleft,res);
        } else { // arr[mid] >= leftmost
            if(arr[mid]<tag){
                rotated(arr,mid+1,R,tag,arr[mid+1],rightmost,goleft,res);
            } else {
                binary(arr,L,mid-1,tag,res);
            }
        }
    } else { // result sits in right side
        if(arr[mid] <= rightmost){
            if(arr[mid]<tag){
                binary(arr,mid+1,R,tag,res);
            } else {
                rotated(arr,L,mid-1,tag,leftmost,arr[mid-1],goleft,res);
            }
        } else { // arr[mid] >= leftmost
            rotated(arr,mid+1,R,tag,arr[mid+1],rightmost,goleft,res);
        }
    }
}
/*
A normal recursive approach considering duplicates
*/
int search(int* arr, const int N, const int tag)
{
    int res, leftmost, rightmost;
    if(N<1) return -1;
    if(N<2) return arr[0]==tag ? 0:-1;
    
    res = -1;
    leftmost = arr[0];
    rightmost= arr[N-1];
    
    if(leftmost < rightmost){
        // normal binary search
        binary(arr,0,N-1,tag, &res);
        return res;
    } else {
        if(tag >= leftmost) rotated(arr,0,N-1,tag,leftmost,rightmost,1,&res);
        else if(tag <= rightmost) rotated(arr,0,N-1,tag,leftmost,rightmost,0,&res);
        return res;
    }
}
/*
An iterative approach by finding the "bend point" first
*/
int search_iter(int* arr, const int N, const int tag)
{
    int res, leftmost, rightmost, lt, rt, mid, bendInd;
    if(N<1) return -1;
    if(N<2) return arr[0]==tag ? 0:-1;
    
    res = -1;
    leftmost = arr[0];
    rightmost= arr[N-1];
    
    if(leftmost < rightmost)
    {
        // normal binary search
        binary(arr,0,N-1,tag, &res);
        return res;
    }
    
    // fine "bend point"
    lt = 0;
    rt = N-1;
    bendInd = -1;
    while(lt < rt)
    {
        mid = (lt+rt) >> 1;
        if((mid - 1 > -1 && arr[mid - 1] <= arr[mid]) &&
           (mid + 1 < N  && arr[mid + 1] <  arr[mid])
        ){
            bendInd = mid;
            break;
        } 
        else if(arr[mid] >= leftmost)
            lt = mid+1;
        else // arr[mid] <= rightmost
            rt = mid-1;
    }
    // if not found, assign lt as bend point
    if(bendInd == -1) bendInd = lt;
    
    // search
    if(
        tag > arr[bendInd] ||
        tag < arr[bendInd + 1] ||
        tag < leftmost && tag > rightmost
    ) return res;
    
    if(tag <= arr[bendInd] && tag >= leftmost) binary(arr,0,bendInd,tag,&res);
    else // (tag >= arr[bendInd+1] && tag <= rightmost)
        binary(arr,bendInd+1,N-1,tag,&res);
	return res;
}
/*
Tester
*/
#define N 15
void test_recursive(void)
{
	int t1[N];// Duplicated
    int i,cut;
    
	// rotated array
	cut = 6;
    for(i=cut;i<N;i++) t1[i] = i + i%2;
    for(i=0;i<cut;i++) t1[i] = i+N + i%2;
    dump(t1,N);

	printf("Search for rotated sorted array (Duplicated):\n");
	printf("%d: %d\n",-1,search(t1,N,-1));
	printf("%d: %d\n",N+cut,search(t1,N,N+cut));
	for(i=cut;i<N;i++){
		printf("%d: %d\n",i,search(t1,N,i));
	}
	for(i=0;i<cut;i++){
		printf("%d: %d\n",i+N,search(t1,N,i+N));
	}
}
void test_iterative(void)
{
    int t1[N];// Duplicated
    int i,cut;
    
	// rotated array
	cut = 6;
    for(i=cut;i<N;i++) t1[i] = i + i%2;
    for(i=0;i<cut;i++) t1[i] = i+N + i%2;
    dump(t1,N);

	printf("Search for rotated sorted array (Duplicated):\n");
	printf("%d: %d\n",-1,search_iter(t1,N,-1));
	printf("%d: %d\n",N+cut,search_iter(t1,N,N+cut));
	for(i=cut;i<N;i++){
		printf("%d: %d\n",i,search_iter(t1,N,i));
	}
	for(i=0;i<cut;i++){
		printf("%d: %d\n",i+N,search_iter(t1,N,i+N));
	}
}
int main(int argc, char* argv[])
{
    //test_recursive();
    test_iterative();
    return 0;
}
