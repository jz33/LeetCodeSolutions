char* addBinary(char* a, char* b)
{
    char *at = a,*bt = b,*rt;
    size_t al = 0, bl = 0, rl;
    int i,j,c=0,s;

    // move to least significant bits
    // count length
    while(*at != '\0')
    {
        at++;
        al++;
    }
    at--;
    while(*bt != '\0')
    {
        bt++;
        bl++;
    }
    bt--;

    // return length
    rl = (al > bl ? al : bl) + 1;
    rt = (char*)malloc(sizeof(char)*(rl+1));
    i=0;
    
    // terminate by '\0'
    while(i < rl)
    {
        rt++;
        i++;
    }
    *rt-- = '\0';

    // sum from right
    i = al - 1;
    j = bl - 1;
    while(i != -1 && j != -1)
    {
        s = c + *at---'0' + *bt---'0';
        c = s >> 1;
        *rt-- = (s & 1) + 48; // notice the operator precedence!
        i--,j--;
    }

    // rest
    while(i != -1)
    {
        s = c + *at---'0';
        c = s >> 1;
        *rt-- = (s & 1) + 48;
        i--;
    }
    while(j != -1){
        s = c + *bt---'0';
        c = s >> 1;
        *rt-- = (s & 1)+48;;
        j--;
    }

    // return
    if(c == 1){
        *rt = '1';
        return rt;
    } else {
        *rt = '\0';
        return rt+1;
    }
}

int main(int argc, char* argv[])
{
    char *a, *b, *c;
    if(argc < 3) return 0;
    a = argv[1]; puts(a);
    b = argv[2]; puts(b);

    c = addBinary(a,b);
    puts(c);
    return 0; 
}
