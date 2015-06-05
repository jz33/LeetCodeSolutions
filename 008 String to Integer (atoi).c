#include <stdio.h>
/*
08 String to Integer (atoi)
https://oj.leetcode.com/problems/string-to-integer-atoi/
*/
int _atoi(const char* str){
    char sign = 0;
    int z = 0;
    if (*str == '-'){
        sign = 1;
        str++;
    }
    while (*str != '\0'){
        if (*str >= '0' && *str <= '9')
            z = z * 10 + *str - '0';
        str++;
    }
    return sign == 0 ? z : -z;
}

int main()
{
    char* x = "-123456789";
    printf("%d\n",_atoi(x));
    return 0;  
}
