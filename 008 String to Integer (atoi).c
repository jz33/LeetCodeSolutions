#include <stdio.h>
/*
08 String to Integer (atoi)
https://oj.leetcode.com/problems/string-to-integer-atoi/
*/
int _atoi(char* str) {
    char sign = 0;
    int z = 0;
    while(*str == ' ') str++;
    if (*str == '-'){
        sign = 1;
        str++;
    } else if (*str == '+') {
        str++;
    } else if (*str < '0' || *str > '9') {
        return 0;
    }
    while (*str != '\0' && *str >= '0' && *str <= '9' ){
        if (!sign && z > INT_MAX / 10) return INT_MAX;
        if (!sign && z == INT_MAX / 10 && *str -'0' >= 7) return INT_MAX;
        if (sign && -z < INT_MIN / 10) return INT_MIN;
        if (sign && -z == INT_MIN / 10 && *str -'0' >= 8) return INT_MIN;
        
        z = z * 10 + *str - '0';
        str++;
    }
    return sign? -z : z;
}

int main()
{
    char* x = "-123456789";
    printf("%d\n",_atoi(x));
    return 0;  
}
