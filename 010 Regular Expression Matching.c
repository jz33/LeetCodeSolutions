#include <stdio.h>
#include <string.h>
/*
10 Regular Expression Matching
https://oj.leetcode.com/problems/regular-expression-matching/
'.' matches any single char
'*' matches 0 or more previous char
O(2^N!), N is '*' numbers
*/
int isMatch(char* tag,char* pat)
{
    int res = 0;

    // base case
    if(*pat == '\0' ) 
        return *tag == '\0';
    if(*tag == '\0' )
        return strlen(pat) == 2 && *(pat+1) == '*';
            
    if(*(pat+1) != '*')
    {
        if(*pat == '.' || *pat == *tag) 
            res = isMatch(tag+1,pat+1);
    } 
    else 
    {
        // 0. skip '*'
        res = isMatch(tag,pat+2);
        
        // 1. '*' matches more than 1 chars
        if(res == 0)
            if(*pat == '.' || *pat == *tag) 
                res = isMatch(tag+1,pat);
    }
    return res;
}

int main()
{
    char* pat = ".*";
    char* tag = "a";
    printf("%d\n",isMatch(tag,pat));
    return 0;  
}
