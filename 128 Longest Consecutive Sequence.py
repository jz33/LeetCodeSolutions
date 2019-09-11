'''
128 Longest Consecutive Sequence.py
https://oj.leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Hashmap, Array
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
