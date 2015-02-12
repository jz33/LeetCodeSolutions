#include <stdio.h>
/*
08 String to Integer (atoi)
https://oj.leetcode.com/problems/string-to-integer-atoi/
*/
/*
int can be minus !
*/
int _atoi(char* p){
    int s = *p == '-' ? -1:1;
	int r = 0;
    
    if(s==-1) p++;
	while(*p != '\0'){
		r = r*10+*p-'0';
		p++;
	}
	return r*s;
}

int main(){
    char* x = "-123456789";
    printf("%d\n",_atoi(x));
    return 0;  
}