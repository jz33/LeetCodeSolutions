/*
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
*/
class Solution {
public:
    int hammingDistance(int x, int y) {
        /*
        There are cerntainly better masking methods
        */
        const int z = (x ^ y);
        int h = 0;
        for (int i = 0, j = 1; i < 31; ++i, j <<= 1) {
            if ((j & z) > 0) {
                h += 1;
            }             
        } 
        return h;
    }
};
