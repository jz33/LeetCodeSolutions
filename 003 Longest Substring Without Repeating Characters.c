#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHAR_BUFFER_SIZE 256
#define MAX(a,b) (a)>(b)?(a):(b)
/*
03 Longest Substring Without Repeating Characters
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
*/
/*
A random string generator
*/
int randInt(const int limit)
{
    int div = RAND_MAX/(limit+1);
    int res = -1;
    do{ 
        res = rand() / div;
    }while (res > limit);
    return res;
}
void randStr(char* in)
{
    int choice;
    while(*in != '\0'){
        choice = randInt(2);
        if(choice == 0){
            *in++ = randInt(9)+'0';
        } else if(choice == 1){
            *in++ = randInt(25)+'A';
        } else {
            *in++ = randInt(25)+'a';
        }
    }
}
/*
Normal O(n^2) approach
*/
void longestSubstringNoDuplicate2(char* in){
    size_t st = 0; // track
    size_t rs = 0,maxLen = 1; // result
    size_t i,j,len = strlen(in);

    for(i=1;i<len;i++){
        for(j=st;j<i;j++){
            if(in[j]==in[i]){
                // update result
                if(i-st > maxLen){
                    rs = st;
                    maxLen = i-st;
                }
                st = j+1;
                break;
            }
        }
    }
    if(i-st > maxLen){
        rs = st;
        maxLen = i-st;
    }
    
    // print result
	printf("%u,%u\n",rs,maxLen);
    for(i=0;i<maxLen;i++) printf("%c",in[i+rs]);
	printf("\n");
}
/*
O(n) time, O(256) buffer approach
*/
void longestSubstringNoDuplicate(char* in){
    int len = (int)strlen(in);
    int st = 0, curLen = 1, maxLen = 1;
    int i, prev;
    /*
    A buffer records char index + 1 of "in"
    */
    int* buf = (int*)calloc(CHAR_BUFFER_SIZE,sizeof(int));
    buf[in[0]] = 1;
    for(i = 1;i<len;i++){
        prev = buf[in[i]]-1;
        if(prev == -1 || i - prev > curLen)
            curLen++;
        else{
            if(curLen > maxLen){
                st = i - curLen;
                maxLen = curLen;
            }
            curLen = i - prev;
        }
        buf[in[i]] = i+1;
    }
    if(curLen > maxLen){
        st = i - curLen;
        maxLen = curLen;
    }      
    free(buf);
    // print result
    for(i=0;i<maxLen;i++) printf("%c",in[i+st]);
	printf("\n");
}
// tester
int main(){
    int i,repeat = 3;
    size_t N = 50;
    char* in = (char*)malloc(sizeof(char)*(N+1));
    in[N] = '\0';
    for(i=0;i<repeat;i++){
        randStr(in);
		puts(in);
        printf("%d: ",i);
		longestSubstringNoDuplicate2(in);
        longestSubstringNoDuplicate(in);
        printf("\n");
    }
    free(in);
    return 0;  
}