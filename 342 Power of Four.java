/*
Power of Four
https://leetcode.com/problems/power-of-four/
*/
public boolean isPowerOfFour(int n) {
    return (Math.log10(n) / Math.log10(4)) % 1 == 0;
}
