#include <stdio.h>
#include <stdlib.h>
/*
15 3Sum
https://oj.leetcode.com/problems/15 3Sum/
*/
int compInt(const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
void sum3(int* arr, const int N){
    int k = 0,i,j;
    int lt,rt,md;
    
    qsort(arr,N,sizeof(int),compInt);
    while(k<N-2){
        lt = arr[k];
        i = k+1;
        j = N-1;
        while(i<j){
            md = arr[i];
            rt = arr[j];
            if(lt+md+rt==0){
                printf("(%d,%d,%d)\n",lt,md,rt);
                i++;
                while(i<j && arr[i]==md) i++;
                j--;
                while(i<j && arr[j]==rt) j--;
			}
            else if(lt+md+rt<0){
                i++;
                while(i<j && arr[i]==md) i++;
            }
            else{
                j--;
                while(i<j && arr[j]==rt) j--;
            }
        }
        k++;
        while(k<N-2 && arr[k]==lt) k++;
    }
    printf("\n\n");
}

int main(){
	//TODO: tests
    return 0; 
}