bool isPalindrome(int x)
{
    int y;
    if(x == 0) return true;
    if(x < 0) return false;
    
    // 10, 100, 1000 ...
    if(x % 10 == 0) return false;
    
    y = 0;
    while(x > y)
    {
        y = y * 10 + x % 10;
        
        // odd
        if(x == y)
            return true;
        
        // x has to be reduced, in case of overflow of y
        x = x / 10; 
    }
    // even
    return x==y;
}
