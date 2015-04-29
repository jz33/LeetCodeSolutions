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
Particularly for this question, assume:
0. array is sorted
1. no duplicates
2. only 1 pair of answer
'''
def twoSum(numbers,target):
    res = [-1,-1]
    for i in xrange(0,len(numbers)):
        r = target - numbers[i]
        if r > 0:
            for j in xrange(i+1,len(numbers)):
                if numbers[j] == r:
                    res[0] = i+1
                    res[1] = j+1
                    return res
    return res
'''
Normal 2 sum problem
'''
def twoSumNormal(numbers,target):
    numbers = sorted(numbers)
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
     
def main():
    numbers = createRandList(16,0,8)
    twoSumNormal(numbers,10)
     
if __name__ == '__main__':
    main()
