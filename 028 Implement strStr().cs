int StrStr(string haystack, string needle) {
    int h = 0;
    int n = 0;
    for(; h <= haystack.Length - needle.Length;h++){
        for(; n < needle.Length;n++){
            if (haystack[h+n] != needle[n]) break;
        }
        if (n == needle.Length) return h;
        n = 0;
    }
    return -1;
}
