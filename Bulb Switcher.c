#include <math.h>
/*
Bulb Switcher
https://leetcode.com/problems/bulb-switcher/
*/
int isSqured(int n){
    int r = (int)sqrt((double)n);
    return n == r*r;
}

int bulbSwitch(int n) {
    int ctr = 0;
    for(int i = 1;i<=n;i++){
        if(isSqured(i)){
            ctr++;
        }
    }
    return ctr;
}
