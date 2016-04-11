'''
Standard KMP for strstr
'''
def strstr(hay, ndl):
    h_len = len(hay);
    n_len = len(ndl);
    if n_len == 0: return 0;
    if n_len == 1: return 0 if h_len > 0 and hay[0] == ndl[0] else -1;
    
    T = [None] * n_len
    T[0] = -1;
    T[1] = 0;
    
    i = 0; # iterate ndl
    j = 2; # iterate table
    while j < n_len:
        if ndl[j - 1] == ndl[i]:
            # T[j++] = ++i;
            i += 1
            T[j] = i;
            j += 1
        elif i > 0:
            i = T[i];
        else:
            T[j] = 0;
            j += 1

    i = 0; # iterate ndl
    j = 0; # iterate hay
    while i + j < h_len:
        if hay[i + j] == ndl[i]:
            i += 1
            if i == n_len:
                return j
        elif i > 0:
            j = j + i - T[i]
            i = T[i]
        else:
            i = 0;
            j += 1;
    return -1

hay = "aaa"
ndl = "a"
print strstr(hay,ndl)
