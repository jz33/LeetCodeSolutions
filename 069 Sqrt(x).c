#include <stdio.h>
#include <stdlib.h>
/*
69 Sqrt(x)
https://oj.leetcode.com/problems/sqrtx/
*/

#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

/*
SQRT
http://en.wikipedia.org/wiki/Fast_inverse_square_root
http://h14s.p5r.org/2012/09/0x5f3759df.html
http://www.codeproject.com/Articles/69941/Best-Square-Root-Method-Algorithm-Function-Precisi
*/
float sqrt0(float number ){
	long i;
	float y;
    
	y  = number;
	i  = * ( long * ) &y;  
	i  = 0x5f3759df - ( i >> 1 );
	y  = * ( float * ) &i;
	y  = y * ( 1.5F - ( number * 0.5F * y * y ) );
//  y  = y * ( 1.5F - ( x2 * y * y ) );   // optional
	return y;
}
/*
A fixed point function used for sqrt & cbrt
Translated from Scala version
*/
float fixedPoint(float (*func)(float,float), float x, float guess, const float epsilon){
    float next = guess;
    do{
        guess = next;
        next = (*func)(x, guess); //printf("next: %f\n",next);
    } while(guess-next > epsilon || next-guess > epsilon);
    return next;
}
float sqrtIter(float x, float y){
    return (y + x / y)/2;
}
float cbrtIter(float x, float y){
    return (y * 2 + x / y / y) / 3;
}
float sqrtFixedPoint(float x){
    return fixedPoint(sqrtIter,x,1,0.01);
}
float cbrtFixedPoint(float x){
    return fixedPoint(cbrtIter,x,1,0.01);
}

int main(){
	// TODO: test
    return 0; 
}