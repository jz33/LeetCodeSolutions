#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
77 Combinations
https://oj.leetcode.com/problems/combinations/
*/
void dumpCharArray(char* A, const int size)
{
    int i = 0;
	for(;i<size;i++) printf("%c ", A[i]);printf("\n");
}
void swap (char *x, char *y)
{
    char t;
    t  = *x;
    *x = *y;
    *y = t ;
}
/*
"i" can be understood like "level"
"swapRange" can be understood like node count from left to right in current level
For example, "ABCD":
0:                         ABCD
1:             ABCD                 BACD      CBAD     DBCA
2:    ABCD     ACBD     ADCB     BCAD  BDCA   CDAB
3: ABCD ABDC   ACDB            BCDA
*/
void combinations(char *a, int i, int swapRange, const int s, const int r)
{
    int j; 
	for(j=swapRange+i;j<s;j++){
		swap((a+i), (a+j));
		if(i+1 == r) dumpCharArray(a,r);
		else combinations(a, i+1, j-i, s, r);
		swap((a+i), (a+j)); 
	}
}
void testCombinations(void)
{
   const int s = 6;
   const int r = 4;
   int i;
   char* ori = (char*)malloc(sizeof(char)*(s+1));
   char* in  = (char*)malloc(sizeof(char)*(s+1));
   for(i = 0;i<s;i++){
	   ori[i] = i+65;
   }
   ori[s] = '\0';
    
   strncpy(in,ori,s+1);
   combinations(in,0,0,s,r);
   
   free(ori);
   free(in);
}
int main(int argc, char** argv)
{
    testCombinations();
    return 0;
}