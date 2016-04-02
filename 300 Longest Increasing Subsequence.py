
'''
300 Longest Increasing Subsequence
'''
def longestIncreasingSubsequenceSize(arr):
    '''
    @return: max length
    '''
    length = len(arr)
    seq = []

    def ceiling(tag):
        '''
        Find the leftmost element in sorted array
        that is larger or equal to tag
        @return : size of longsest
        '''
        lt = 0
        rt = len(seq) - 1
        while lt <= rt:
            mid = (lt + rt >> 1);
            v = seq[mid];
            if v == tag: return -1;
            elif v < tag: lt = mid + 1;
            else: rt = mid - 1;
        return lt;

    for e in arr:
        if len(seq) == 0 or seq[-1] < e:              
            seq.append(e)
        else:
            j = ceiling(e);
            if j > -1: seq[j] = e
    return len(seq)

def longestIncreasingSubsequence(arr):
    '''
    https://en.wikipedia.org/wiki/Longest_increasing_subsequence
    @return: actual subarray
    '''
    length = len(arr)
    seq = [] # index buffer
    par = [None] * length # parent indexes

    def ceiling(tag):
        '''
        Find the leftmost element in sorted array
        that is larger or equal to tag
        @return : size of longsest
        '''
        lt = 0
        rt = len(seq) - 1
        while lt <= rt:
            mid = (lt + rt >> 1);
            v = arr[seq[mid]];
            if v == tag: return -1;
            elif v < tag: lt = mid + 1;
            else: rt = mid - 1;
        return lt;

    for i,e in enumerate(arr):
        if len(seq) == 0:
            par[i] = -1           
            seq.append(i)
        elif arr[seq[-1]] < e:
            par[i] = seq[-1]
            seq.append(i)
        else:
            j = ceiling(e)
            if j == 0:
                par[i] = -1
            elif j > -1: 
                par[i] = seq[j-1]
                seq[j] = i

    res = [None] * len(seq)
    j = seq[-1]
    for i in xrange(len(seq)-1,-1,-1):
        res[i] = arr[j]
        j = par[j]
    return res

# arr = [2,6,3,4,1,2,9,5,8]
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
size = longestIncreasingSubsequenceSize(arr)
print size
res = longestIncreasingSubsequence(arr)
print res
