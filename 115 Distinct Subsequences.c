#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
115 Distinct Subsequences
https://oj.leetcode.com/problems/distinct-subsequences/
*/
int distinctSequences(char* a, char* b)
{
    int i,j;
    int* row;
    int upper, upperLeft;
    int la = (int)strlen(a);
    int lb = (int)strlen(b);
    if(la==0 || lb > la) return 0;
    if(lb==0) return 1;
	
    row = (int*)calloc(lb+1,sizeof(int));
    
    for(i=0;i<la;i++)
    {
        upperLeft = 1;
        for(j=0;j<lb;j++)
        {
            upper = row[j+1];
            if(a[i] == b[j]) row[j+1] += upperLeft;
            upperLeft = upper;
        }
    }
    i = row[lb];
    free(row);
    return i;
}

int main()
{
    char* src = 'rabbbit';
    char* tag = 'rabbit';
    printf("%d\n",distinctSequences(src,tag));
    return 0;
}
