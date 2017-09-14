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
