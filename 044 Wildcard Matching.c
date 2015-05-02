#include <stdio.h>
/*
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/

'?' matches any single char
'*' matches 0 or more any chars
*/
int isMatch(char* tag, char* pat)
{
    int res = 0; 
    
    // bottom case
    if(*pat == '\0' ) return *tag == '\0';
    if(*tag == '\0' ) return *pat == '*';
    
    if(*pat == '?' || *pat == *tag)
        return isMatch(tag+1, pat+1);
        
    else if (*pat == '*')
    {
        // 0. skip '*'
        res = isMatch(tag,pat+1); 
        
        // 1. '*' matches only 1 char 
        if(res == 0)
            res = isMatch(tag+1,pat+1);
            
        // 2. '*' matches more than 1 chars
        if(res == 0)
            if(*(tag+1) == *tag) 
                res = isMatch(tag+1,pat);
    }
    return res;
}

int main()
{
    char* tag = "aab";
    char* pat = "a*a*b";   
     
    printf("%d\n",isMatch(tag,pat));
    return 0;
}
