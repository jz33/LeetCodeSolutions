#include <stdio.h>
#include <stdlib.h>
/*
67 Add Binary
https://oj.leetcode.com/problems/add-binary/
*/
#define MAX(a,b) (a)>(b)?(a):(b)

char* binaryPlus(char* a, char* b){
    char *at = a,*bt = b,*rt;
    size_t al = 0, bl = 0, rl;
    int i,j,c=0,s;
    
    while(*at != '\0'){
        at++;
        al++;
    }
    at--;
    
    while(*bt != '\0'){
        bt++;
        bl++;
    }
    bt--;
    
    rl = MAX(al,bl)+1;
    rt = (char*)malloc(sizeof(char)*(rl+1));
	i=0;
    while(i<rl){
        rt++;
        i++;
    }
    *rt-- = '\0';
    
    i = al-1;
    j = bl-1;
    while(i != -1 && j != -1){
        s = c + *at---'0'+*bt---'0';
        c = s >> 1;
        *rt-- = (s & 1)+48; // notice the operator precedence!
		i--,j--;
    }
    
    while(i != -1){
        s = c+*at---'0';
        c = s >> 1;
        *rt-- = (s & 1)+48;
		i--;
    }
    
    while(j != -1){
        s = c+*bt---'0';
        c = s >> 1;
        *rt-- = (s & 1)+48;;
		j--;
    }
    
    if(c == 1){
        *rt = '1';
        return rt;
    } else {
		*rt = '\0';
        return rt+1;
    }
}

int main(){
	// TODO: test
    return 0; 
}