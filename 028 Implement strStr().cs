int StrStr(string haystack, string needle) {
    for(int h = 0; h <= haystack.Length - needle.Length;h++){
        int n = 0;
        for(; n < needle.Length;n++){
            if (haystack[h+n] != needle[n]) break;
        }
        if (n == needle.Length) return h;
    }
    return -1;
}
