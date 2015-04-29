#include <stdio.h>
#include <stdlib.h>
/*
31 Next Permutation
https://oj.leetcode.com/problems/next-permutation/
http://yucoding.blogspot.com/2013/04/leetcode-question-61-next-permutation.html
http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
*/
int compChars(const void * a, const void * b)
{
  return (*(char*)a - *(char*)b);
}
void swapChars(char* a, char* b){
    char t = *a;
    *a = *b;
    *b = t;
}
void reverse(char* str){
    char* p = str;
    char* q = str;
    
    while(*q != '\0') q++;
    q--;
    
    while(p < q) swapChars(p++,q--);
}

void nextPermutation(char* str){
    char* lt = 0;
    char* rt = 0;
    char* p = str;
    
    /*
    1. Find the largest index 'lt' such that
    str[lt+1] > str[lt]
    */
    p++;
    while(*p != '\0'){
        if(*(p-1)<*p) lt = p;
        p++;
    }
    if(lt == 0){
        reverse(str);
        return;
    }
	lt--;
    
    /*
    2. Find the largest index 'rt' such that
    str[rt] > str[lt]
    */
    p = lt+1;
    while(*p != '\0'){
        if(*p >= *lt) rt = p;
        p++;
    }
    
    /*
    3. Swap, reverse
    */
    swapChars(lt,rt);
    reverse(lt+1);
}

int main(){
	char* str = (char*)malloc(sizeof(char)*4);
    
    str[0] = '1';str[1]= '2';str[2]='3';str[3]='\0';
    nextPermutation(str);puts(str);
    
    str[0] = '3';str[1]= '2';str[2]='1';str[3]='\0';
    nextPermutation(str);puts(str);
    
    str[0] = '1';str[1]= '1';str[2]='5';str[3]='\0';
    nextPermutation(str);puts(str);
    
    free(str);
}
