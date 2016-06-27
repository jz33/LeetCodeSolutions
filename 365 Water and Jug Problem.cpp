#include <cmath>
/**
 * 0 < x < z < y or 0 < z < x < y
 * yi - xj = z, get integer solution of i, j
 * or xi - yj = z
 */
bool inner(int x, int y, int z) {
    int i;
    for(i = 1;i<x;i++) {
        if((y * i - z) % x == 0) {
            return true;
        }
    }
    for(i = (int)(ceil(z / x)); i<y; i++) {
        if((x * i - z) % y == 0) {
            return true;
        }
    }
    return false;
}

bool canMeasureWater(int x, int y, int z) {
    int k;
    if(x > y) {
        k = x; x = y; y = k;
    }
    if(z > x + y) {
        return false;
    }
    if(z == 0) {
        return true;
    }
    if(x == 0) {
        return z == y;
    }
    if(z == x || z == y || z == x + y || z == y - x) {
        return true;
    }
    if(z > y) {
        return inner(x,y,z-y) || inner(x,y,z-x);
    } else {
        return inner(x,y,z);
    }
}
