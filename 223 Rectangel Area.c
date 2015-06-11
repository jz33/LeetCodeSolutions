#include <stdio.h>
/*
223 Rectangle Area
https://leetcode.com/problems/rectangle-area/
(A,B) lower-left
(C,D) upper-right
*/
int dist(int x, int y){
    return x - y > 0 ? x - y : y - x;
}
/*
0. Only (A,B) inside EFGH: 
area -= (G - A) * (H - B);
1. Only (A,B), (A,D) inside EFGH
area -= (G - A) * (D - B);
2. Only (A,B), (C,B) inside EFGH
area -= (C - A) * (H - B);
3. ABCD inside EFGH
area -= (C - A) * (D - B);
*/
#define Compare(area,A,B,C,D,E,F,G,H)\
    if((A >= E && A <= G || A <= E && A >= G )&&(B >= F && B <= H || B <= F && B >= H)){\
        int ca = dist(C,A);\
        int ga = dist(G,A);\
        int db = dist(D,B);\
        int hb = dist(H,B);\
        return area - (ca < ga ? ca : ga) * (db < hb ? db: hb);\
    }

int computeArea(int A, int B, int C, int D, int E, int F, int G, int H)
{
    int area = (C - A)*(D - B) + (G - E )*(H - F);
    
    Compare(area,A,B,C,D,E,F,G,H);
    Compare(area,C,B,A,D,G,F,E,H);
    Compare(area,C,D,A,B,G,H,E,F);
    Compare(area,A,D,C,B,E,H,G,F);
    
    Compare(area,E,F,G,H,A,B,C,D);
    Compare(area,G,F,E,H,C,B,A,D);
    Compare(area,G,H,E,F,C,D,A,B);
    Compare(area,E,H,G,F,A,D,C,B);
    
    // non-overlap
    return area;
}
void test(void)
{
    int arr[] = {-2,-2,2,2,-1,-1,1,1};//16
    //int arr[] = {2,2,3,3,-2,-2,2,2};//17
    //int arr[] = {-2,-2,2,2,2,2,3,3};//17
    //int arr[] = {-2, -2, 2, 2, 1, -3, 3, -1}; // 19

    int r = computeArea(\
        arr[0],arr[1],arr[2],arr[3],\
        arr[4],arr[5],arr[6],arr[7]);
    
    printf("%d\n",r);
}
int main()
{
    test();
    return 0;
}
