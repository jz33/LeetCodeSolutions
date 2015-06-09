#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
28 Implement strStr()
https://oj.leetcode.com/problems/implement-strstr/
*/
// A normal brutal-force approach
char* _strstr(char* haystack, char* needle){
    register char *pr = 0; 
    register char *psub = 0; // sub

    while(*(pr=haystack++) != '\0'){
        psub = (char*)needle;
        while(*pr!='\0' && *psub!='\0' && *pr==*psub) pr++, psub++;
        if(*psub=='\0') return haystack-1;
    }
    
    // clean up, not found, return pl
    return pr, psub=0;
}

// KMP
int _kmp(char* hay, char* ndl)
{ 
    int* T;
    int i,j;
    
    size_t h_len = strlen(hay);
    size_t n_len = strlen(ndl);
    if(h_len == 0 && n_len == 0) return 0;
    if(h_len == 1 && n_len == 0) return 0;
    if(h_len == 0 && n_len == 1) return -1;
    if(h_len == 1 && n_len == 1) return hay[0] == ndl[0] ? 0:-1;
    
    // 1. Build Table
    T = (int*)malloc(sizeof(int)*n_len);
    T[0] = -1;
    T[1] = 0;
    
    i = 2; // iterate ndl
    j = 0; // iterate over T
    while(i < n_len)
    {
        if(ndl[i-1] == ndl[j])
            T[i++] = ++j;
        else if (j>0)
            j = T[j];
        else 
            T[i++] = 0;
	}

    // 2. Compare
    i = 0; // iterate ndl
    j = 0; // iterate hay
    while(i+j < h_len)
    {
        if(hay[j+i] == ndl[i])
        {
            if(i++ == n_len -1)
            {
                free(T);
                return j;
            }
        }
        else
        {
            if(T[i] > -1)
            {
                j = j+i-T[i];
                i = T[i];
            }
            else
            {
                i = 0;
                j++;
            }
        }
    }
    
    free(T);
    return -1;
}

void test_strstr(void)
{
    char* hay = "ABC ABCDAB ABCDABCDABDE";
    char* ndl = "ABCDABD";
    puts(_strstr(hay,ndl));
    printf("%d\n",_kmp(hay,ndl));
}

int main()
{
    test_strstr();
    return 0;
}
