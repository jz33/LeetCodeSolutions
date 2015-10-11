/*
Length of Last Word
https://leetcode.com/problems/length-of-last-word/
*/
int lengthOfLastWord(char* r) {
    int c;
    if(r == 0) return 0;
    
    while(*r != '\0'){
        while(*r != '\0' && *r == ' ') r++;
        if(*r == '\0') return c;
        
        c = 0;
        
        while(*r != '\0' && *r != ' ') r++,c++;
        if(*r == '\0') return c;
    }
    return 0;
}
