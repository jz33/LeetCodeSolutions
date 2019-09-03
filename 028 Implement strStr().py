def kmpTable(needle: str) -> List[str]:

    # T[i] is the length of the longest proper prefix of ndl[:i+1]
    # which is also the suffix of ndl[:i+1]
    # T[0] is always 0
    n_len = len(needle)
    T = [0] * n_len
    
    ll = 0; # The length of the previous longest prefix suffix
    i = 1; # Iterator of T
    while i < n_len:
        if needle[i] == needle[ll]:
            # If current char matches ll-th char from beginning of needle,
            # and because needle[:ll] == needle[i-ll:i],
            # therefore needle[:ll+1] == needle[i-ll:i+1]
            ll += 1
            T[i] = ll;
            i += 1
        elif ll > 0:
            # No match, try to reduce ll to see if matching
            ll = T[ll-1];
        else:
            # No match no matter what, move on
            # T[i] = 0, by default
            i += 1

    return T

def kmpSearch(haystack: str, needle: str) -> int:
    h_len = len(haystack);
    n_len = len(needle);
    if n_len == 0:
        return 0;
    if n_len == 1:
        return 0 if h_len > 0 and haystack[0] == needle[0] else -1

    T = kmpTable(needle)

    ni = 0; # Iterator of needle
    hi = 0; # Iterator of haystack 
    while ni + hi < h_len:
        if haystack[ni + hi] == needle[ni]:
            # Keep matching
            ni += 1
            if ni == n_len:
                return hi
        elif ni > 0:
            # Mismatch, move both hi and ni
            hi += ni - T[ni-1] 
            ni = T[ni-1]
        else:
            # No match no matter what, reset
            hi += 1;

    return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmpSearch(haystack, needle)
        
