#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
151 Reverse Words in a String
https://oj.leetcode.com/problems/reverse-words-in-a-string/
*/
/*
No extra buffer approach

s0,s1 ->
"Bravo ms Kane"
"Kane ms Bravo"
	  <- r0,r1
*/
void reverseSentence(char* input, char* ret)
{
    int len = (int)strlen(input);
    int ctr;
    
    char* s0 = input;
    char* s1 = input;
    char* r0 = ret;
    char* r1 = ret;

    // 0. move r0,r1 to ret's tail
    ctr = 0;
    while(ctr != len)
    {
        r0++;
        ctr++;
    }
    *r0 = '\0';
	
    while(*s1 != '\0'){
        // 1. move s1 to space, move r0 reversely
        while(*s1 != '\0' && *s1 != ' ')
        {
            s1++;
            r0--;
        }
        // 2. write
        r1 = r0;
        while(s0 != s1){
            *r1++ = *s0++;
        }		
        // 3. assign space
        if(*s1 == '\0') break;
        *--r0 = ' ';
        s0 = ++s1;
    }
}

int main()
{
    char* input = "Bravo ms Kane";
    int len = (int)strlen(input);
    char* ret = (char*)malloc(sizeof(char*)*(len+1));
    reverseSentence(input,ret);
    puts(ret);
    return 0;
}