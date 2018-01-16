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
     
def twoSum(nums, target):
    """
    Sorting way
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    arr = [(i,nums[i]) for i in range(len(nums))]
    arr.sort(key = lambda x:x[1])
    i = 0
    j = len(arr) - 1
    while i < j:
        s = arr[i][1] + arr[j][1] 
        if s == target:
            return (arr[i][0],arr[j][0])
        elif s < target:
            i += 1
        else:
            j -= 1
    return None

def twoSum(self, nums, target):
    """
    Hashtable way
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {}
    for ind,val in enumerate(nums):
        x = target-val
        if x in hashtable:
            return [hashtable[x],ind]
        hashtable[val] = ind
