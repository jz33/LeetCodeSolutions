def wordBreak(tag, book):
    size = len(tag)
    if size == 0: return True
    if tag in book: return True # optional
    
    # 'buf[i]' indicates whether tag[i:] is work break
    buf = [False] *(size+1)
    buf[size] = True
    for i in xrange(size-1,-1,-1):
        for j in xrange(i+1,size+1):
            if tag[i:j] in book and buf[j] is True:
                buf[i] = True
                break
    return buf[0]
