import random
'''
Maximum Gap
https://oj.leetcode.com/problems/maximum-gap/
Bucket sort
'''
DEBUG = True

def creatRandomList(size):
    ls = []
    for i in range(0,size):
        ls.append(random.randint(-size*size,size*size))
    return ls

def maxGap(ls):
    if len(ls) < 2: return 0
    min_total = min(ls,key = int)
    max_total = max(ls,key = int)
    
    length = max_total - min_total
    if length <= 1: return length
    
    min_invalid = min(min_total-1,-max_total)
    max_invalid = max(-min_total,max_total+1)

    if DEBUG:
        print min_total,max_total
        print min_invalid,max_invalid
    
    min_buckets = [max_invalid] * len(ls)
    max_buckets = [min_invalid] * len(ls)

    for val in ls:
        # Notice the cast
        i = int(float(val - min_total) / float(length) * (len(ls) - 1))
        min_buckets[i] = min(min_buckets[i],val)
        max_buckets[i] = max(max_buckets[i],val)

    if DEBUG:
        print min_buckets
        print max_buckets
    
    max_gap = 0
    max_prev = max_buckets[0]
    max_ind = -1
    for i in range(1,len(ls)):
        if min_buckets[i] != max_invalid and max_buckets[i] != min_invalid:
            if min_buckets[i] - max_prev > max_gap:
                max_gap = min_buckets[i] - max_prev
                max_ind = i
            max_prev = max_buckets[i]
    max_gap = max(max_gap, max_total - max_prev)

    if DEBUG: print max_ind, max_gap
    
    return max_gap

#ratings = creatRandomList(3)
#ratings = [3,6,9,1]
#ratings = [1,1,1,1,1,5,5,5,5,5]
ratings = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
print sorted(ratings)
print maxGap(ratings)
