'''
91 Decode Ways
https://oj.leetcode.com/problems/decode-ways/
'''
 
# A recursive approach, "curr" starts from 0
def vocabularyComposeCount(src, curr):
    if curr > len(src)-1 : return 1
    c0 = src[curr]
    if c0 == '0': return 0
    if curr == len(src)-1 : return 1
     
    r0 = vocabularyComposeCount(src,curr+1)
    r1 = 0
     
    c1 = src[curr+1]
    n1 = (int(c0) - int('0'))*10 + int(c1) - int('0')
    if n1 < 27:
        r1 = vocabularyComposeCount(src,curr+2)
    return r0+r1
 
# A tricky DP approach, use only constant memory
def dp(src):
    if len(src) < 1: return 0
    if len(src) == 1: return 0 if src[0] == '0' else 1
    if src[0] == '0': return 0
     
    # the buffer is of size 3
    buf = [1,0,1]
    j = 0
    for i in xrange(1,len(src)):
        j = (j+1) % 3
        n1 = (int(src[i-1]) - int('0'))*10 + int(src[i]) - int('0')
        if src[i] == '0':
            if src[i-1] == '0': return 0
            elif n1 > 26: return 0
            else: buf[j] = buf[j-2]
        else:
            if src[i-1] == '0': buf[j] = buf[j-1]
            elif n1 > 26: buf[j] = buf[j-1]
            else : buf[j] = buf[j-1] + buf[j-2]
    return buf[j]
 
def test_vocabularyComposeCount():
    cases =  ["20","1313","13013","12013","131313","111111","1111001111"]
     
    for src in cases:
        print dp(src), " : ",vocabularyComposeCount(src,0)
         
def main():
    test_vocabularyComposeCount()
 
if __name__ == "__main__":
    main()
