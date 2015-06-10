import random
'''
01 Two Sum
https://oj.leetcode.com/problems/two-sum/
'''
def createRandList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A
'''
Normal 2 sum problem
'''
def twoSumNormal(numbers,target):
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i < j:
        lt = numbers[i]
        rt = numbers[j]
        if lt + rt == target:
            print "(",i,":",j,")"
            i += 1
            while i < j and numbers[i] == lt: i += 1
            j -= 1
            while i < j and numbers[j] == rt: j -= 1
        elif lt + rt < target:
            i += 1
            while i < j and numbers[i] == lt: i += 1
        else:
            j -= 1
            while i < j and numbers[j] == rt: j -= 1
     
'''
Particularly for this question, assume:
0. array is sorted
1. no duplicates
2. only 1 pair of answer
'''
def twoSum(nums, target):
    pairs = [(i,nums[i]) for i in xrange(0,len(nums))]
    pairs = sorted(pairs, key = lambda x : x[1])
    
    i = 0
    j = len(pairs) - 1
    while i < j :
        s = pairs[i][1] + pairs[j][1]
        if s == target:
            x = pairs[i][0]+1
            y = pairs[j][0]+1
            return [x,y] if x < y else [y,x]
        elif s < target:
            i += 1
        else: 
            j -= 1
  
    return [-1,-1]
    
def main():
    numbers = createRandList(16,0,8)
    twoSumNormal(numbers,10)
     
if __name__ == '__main__':
    main()
