#include <stdio.h>
#include <stdlib.h>
/*
18 4Sum
https://oj.leetcode.com/problems/4sum/
*/
int compInt(const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
void sum4(int* arr, const int N){
    int i,j;
    int x = 0, y = N-1;
    int vi,vj,vx,vy,v;
    
    qsort(arr,N,sizeof(int),compInt);
    while(x<y){
        vx = arr[x];
        vy = arr[y];
        v = vx+vy;
        i = x+1;
        j = y-1;
        while(i<j){
            vi = arr[i];
            vj = arr[j];
            if(vi+vj+v==0){
                printf("(%d,%d,%d,%d)\n",vx,vi,vj,vy);
                i++;
                while(i<j && arr[i]==vi) i++;
                j--;
                while(i<j && arr[j]==vj) j--;
			}
            else if(vi+vj+v<0){
                i++;
                while(i<j && arr[i]==vi) i++;
            }
            else{
                j--;
                while(i<j && arr[j]==vj) j--;
            }
        }
        x++;
        while(x<y && arr[x]==vx) x++;
        y--;
        while(x<y && arr[y]==vy) y++;
    }
    printf("\n\n");
}

int main(){
	//TODO: tests
    return 0; 
}