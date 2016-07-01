double mySqrt(double x) {
    double y = 1.0;
    do {
        y = (y + x / y) / 2.0;
    } while(y * y - x > 0.1 || y * y - x < -0.1);
    return y;
}

bool isPerfectSquare(int num) {
    int sq = (int)mySqrt((double)num);
    return sq * sq == num;
}
