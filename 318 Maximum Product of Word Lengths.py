'''
Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/
'''
def hash(word):
    A = ord('a')
    r = 0
    for ch in word:
        r  = (r | (1 << (ord(ch) - A)))
    return r   

def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    # Filter, remove duplicates. May not be necessary
    map = {}
    for w in words:
        h = hash(w)
        map[h] = max(map.get(h,0),len(w))
    
    # Sort. May not be necessary
    ls = sorted(list(map.iteritems()), key = lambda x : x[1], reverse = True)
    
    maxVal = 0
    '''
    From large possible multiplication to small, i.e.,
    if len(ls) == 4:
        0, (0*0)
        1, (1*0)
        2, (2*0),(1*1)
        3, (3*0),(2*1)
        4, (3*1),(2*2), // (4*0)
        5, (3*2) // (5*0),(4*1)
        6, (3*3) // (6*0),(5*1),(4*2)
    
    # Only works if length are distinct
    last = len(ls) - 1
    for i in xrange(0, last * 2):
        maxVal = 0
        for j in xrange(min(last,i), i/2-1, -1):
            (h0,l0) = ls[j]
            (h1,l1) = ls[i-j]
            if (h0 & h1) == 0:
                maxVal = max(maxVal, l0 * l1)
        if maxVal != 0: 
            return maxVal
    '''
    for i in xrange(len(ls)):
        if ls[i][1] * ls[i][1] <= maxVal: break
        for j in xrange(i,len(ls)):
            (h0,l0) = ls[i]
            (h1,l1) = ls[j]
            if (h0 & h1) == 0:
                maxVal = max(maxVal, l0 * l1)
    return maxVal   
    
words = ["debcc","faaeababdc","fdafedb","aaecfeedb","bd","cbdbbeeed","cdbfedadf","bfafbbcf","fabcd","bbefdaaccea","aaaebebcc","fecebb","aee","ddf","daedcaacab","ebcefd","aadbcc","dddbbecfe","aefcfadef","cebceefbbd","bfdcdcadd","cccb","fceefc","ac","fadbebaceea","bbcbdddcba","df","bcacbcfddde","eafacdadcda","ab","faadf","eccaccb","bdbab","aabfb","bdc","edca","aceef","ff","af","ced","ffffbeabfeb","edecbfbdd","acfdfebeadc","ebec","ffdfcc","def","cdebb","bffdacaf","dfbfcacd","dafeaacfd","bddfbbbada","eddcfcd","aeb","dcac","babbcdacec","bd","afc","ebddce","debbb","bddffdddcc","efcbeac","fcbfffe","cfadee","bdefcd","abbeccf","acfacbdb","eeea","dfde","aaaeba","baaafabeeda","fdeedcfaccd","eeabfddccd","bfcd","cedc","aa","dfdfa","aaeaddfaee","bed","affdabcfefe","abdaedb","ccfbac","cc","acd","aabf","efaaeddeee","ebffeab","afeba","cacbfcacaaa","ddedbdfaee","fc","bcfafabdefd","ecbedfcd","acbdfba","bccfdfb","eceb","ffcffeaac","dafe","eed","cadde","afdebe","fd","cfeadac","ccbaeacc"]
print maxProduct(words)       
