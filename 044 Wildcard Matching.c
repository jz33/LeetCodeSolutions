#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/

'?' matches any single char
'*' matches 0 or more any chars
*/
int isMatch(char* tag, char* pat){
    int res = 0; 
    
    // bottom case
    if(*pat == '\0' ) return *tag == '\0';
    if(*tag == '\0' ) return *pat == '*';
    
    if(*pat == '?' || *pat == *tag){
        return isMatch(tag+1, pat+1);
    } else if (*pat == '*'){
        // 0. skip '*'
        res =  isMatch(tag,pat+1); 
        // 1. '*' matches only 1 char 
        res |= isMatch(tag+1,pat+1);
        // 2. '*' matches more than 1 chars
        if(*(tag+1) == *tag) res |= isMatch(tag+1,pat);
    }
    return res;
}

int main()
{
    int N = 10;
    char tag[N];
    char pat[N];
    
    strcpy(tag,"aab");
    strcat(tag,"\0");
    
    strcpy(pat,"c*a*b");
    strcat(pat,"\0");
    
    printf("%d\n",isMatch(tag,pat));
    return 0;
}