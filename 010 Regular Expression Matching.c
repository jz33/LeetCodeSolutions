#include <stdio.h>
/*
10 Regular Expression Matching
https://oj.leetcode.com/problems/regular-expression-matching/

Accepted

'.' matches any single char
'*' matches 0 or more previous char
O(2^N!), N is '*' numbers
*/
bool isMatch(char* s, char* p)
{
    // "" -> ""
    if(*p == '\0') 
        return *s == '\0';
    
    // "" -> "" || ".*.*"
    if(*s == '\0')
        return p[1] == '*' && isMatch(s,p+2);
    
	if(p[1] == '\0' || p[1] != '*')
        return (*p == '.' || *p == *s) && isMatch(s+1,p+1);
    
    // p[1] == '*'
    // 0. skip '*'
    return isMatch(s,p+2) ||
                
    // 1. '*' matches more than 1 chars
    ((*p == '.' || *p == *s) && isMatch(s+1,p));
}

int main()
{
    printf("%u\n",isMatch("ab", ".*c")); // false
    printf("%u\n",isMatch("aa", "a*")); // true
    printf("%u\n",isMatch("", "c*c*")); // true
    return 0;  
}
