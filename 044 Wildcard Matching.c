#include <stdio.h>
#include <string.h>
/*
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/
'?' matches any single char
'*' matches 0 or more any chars

https://leetcode.com/discuss/38645/128ms-o-1-space-python-solution

Accepted
*/
bool isMatch(char* src, char* pat)
{   
    int s,p,ls,lp,prev_s,prev_p;
    if(*pat == '\0' ) return *src == '\0';

    ls = (int)strlen(src);
    lp = (int)strlen(pat);
    s = 0;
    p = 0;
    prev_s = 0;
    prev_p = -1;
    
    while(s < ls)
    {
        if(p < lp && (pat[p] == '?' || pat[p] == src[s]))
        {
            s++;
            p++;
        }
        else if(p < lp && pat[p] == '*')
        {
            prev_s = s;
            prev_p = p++;
        }
        else if(prev_p > -1)
        {
            s = prev_s++ + 1;
            p = prev_p;
        }
        else 
            return 0;
    }
    
    if(s != ls)
        return 0;
    
    while(p < lp && pat[p] == '*')
        p++;
    
    return p == lp;
}
int main()
{
    char* src = "aab";
    char* pat = "a*a*b";   
     
    printf("%d\n",isMatch(src,pat));
    return 0;
}
