#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
72 Edit Distance
https://oj.leetcode.com/problems/edit-distance/
http://rosettacode.org/wiki/Levenshtein_distance#C.2B.2B
*/
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MIN3(x, y, z) ((x) < (y) ? (MIN(x,z)) : (MIN(y,z)))

int LevenshteinDistance(char* a, char* b)
{
    int upper, upperLeft, left;
    int i,j;
    int* row;
    int la = (int)strlen(a);
    int lb = (int)strlen(b);
    if(la == 0) return lb;
    if(lb == 0) return la;
	
    row = (int*)malloc(sizeof(int)*(lb+1));
    for(j = 0;j<lb+1;j++) row[j] = j;
	
    for(i = 0;i<la;i++)
    {
	upperLeft = i;
	left = i+1;
	for(j = 0;j<lb;j++)
	{
	    upper = row[j+1];
	    if(a[i] == b[j]) row[j+1] = upperLeft;
	    else row[j+1] = MIN3(upperLeft,upper,left)+1;
            upperLeft = upper;
	    left = row[j+1];
	}
    }
    i = row[lb];
    free(row);
    return i;
}

int main(int argc, char** argv)
{
    char* a = "abcdef";
    char* b = "abed";
    printf("%i\n",LevenshteinDistance(a,b));
    return 0;
}