/*
https://leetcode.com/problems/sum-of-two-integers/description/
*/
int getSum(int x, int y) {
    int a,b;
    do{
        a=x & y;
        b=x ^ y;
        x=a << 1;
        y=b;
    } while(a);
    return b;
}

// use only 1 var
int getSum(int a, int b) {
    int x;
    do {
        x = a & b;
        b = a ^ b;
        a = x << 1;
    } while (x);
    return b;
}
