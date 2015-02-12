'''
128 Longest Consecutive Sequence.py
https://oj.leetcode.com/problems/longest-consecutive-sequence/

Use a hash map
'''
def longestConsecutive(ls):
    ref = {}
    maxlen = 1
    for n in ls:
        ref[n] = 1
    for n in ls:
        if n in ref:
            nextVal = n + 1
            length  = 1
            while nextVal in ref:
                length +=1
                del ref[nextVal]
                nextVal += 1
            nextVal = n - 1
            while nextVal in ref:
                length +=1
                del ref[nextVal]
                nextVal -= 1
            maxlen = max(length, maxlen)
    return maxlen
    
def main():
    ls = [1,2,4,5,6,8,9]
    print ls
    print longestConsecutive(ls)
    
if __name__ == "__main__":
    main()
