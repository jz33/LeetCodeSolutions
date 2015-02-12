#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
28 Implement strStr()
https://oj.leetcode.com/problems/implement-strstr/
*/
char* _strstr(char* haystack, char* needle){
    register char *pr = 0; 
    register char *psub = 0; // sub

    while(*(pr=haystack++) != '\0'){
        psub = needle;
        while(*pr!='\0' && *psub!='\0' && *pr++==*psub++);
        if(*psub=='\0') return haystack-1;
    }
    
    // clean up, not found, return pl
    return pr, psub=0;
}

int main(){
    char* haystack = "abcdef";
    char* needle = "def";
    puts(_strstr(haystack,needle));
    puts(strstr(haystack,needle));
    return 0;
}
