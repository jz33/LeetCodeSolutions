#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
78 Subsets
https://oj.leetcode.com/problems/subsets/
http://www.geeksforgeeks.org/power-set/

90 Subsets II
https://oj.leetcode.com/problems/subsets-ii/

For 91, i.e., power set with duplicates,
consider using "permuation with duplicates",
see "47 Permutations II"
*/
void power(char *set){
    int set_size = (int)strlen(set);
    int pow_set_size = 1 << set_size;
    int counter, i,j;
    char* buf = (char*)malloc(sizeof(char)*(set_size+1));
    for(counter = 0; counter < pow_set_size; counter++){
        i = 0;
        for(j = 0; j < set_size; j++){
            if(counter & (1<<j)){
                buf[i++] = set[j];
            }
        }
        buf[i] = '\0';
        puts(buf);
    }
    free(buf);
}
int main(int argc, char** argv){
    char* str = "123";
    power(str);
	putchar('\n');
    powerNoDup(str);
    return 0;
}