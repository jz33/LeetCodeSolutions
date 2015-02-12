import random,math
'''
164 Maximum Gap
https://oj.leetcode.com/problems/maximum-gap/

Bucket sort
'''
def creatRandomList(size):
    ls = []
    for i in range(0,size):
        ls.append(random.randint(-size*size,size*size))
    return ls

def maxGap(ls):
    if len(ls) < 2: return 0
    min_total = min(ls,key = int)
    max_total = max(ls,key = int)
    gap = (max_total - min_total) // (len(ls) - 1)
    min_invalid = min(min_total-1,-max_total)
    max_invalid = max(-min_total,max_total+1)

    print min_total,max_total,gap
    print min_invalid,max_invalid
    
    min_buckets = [max_invalid]*len(ls)
    max_buckets = [min_invalid]*len(ls)

    for val in ls:
        i = (val - min_total) // gap
        min_buckets[i] = min(min_buckets[i],val)
        max_buckets[i] = max(max_buckets[i],val)

    print min_buckets
    print max_buckets
    
    max_gap = min_invalid
    max_prev = max_buckets[0]
    max_ind = -1
    for i in range(1,len(ls)):
        if min_buckets[i] != max_invalid and max_buckets[i] != min_invalid:
            if min_buckets[i] - max_prev > max_gap:
                max_gap = min_buckets[i] - max_prev
                max_ind = i
            max_prev = max_buckets[i]
 
    max_gap = max(max_gap, max_total - max_prev)

    print max_ind, max_gap
    
def main():
    ratings = creatRandomList(10)
    print ratings
    print sorted(ratings)
    maxGap(ratings)
    
    
if __name__ == "__main__":
    main()
