'''
Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
http://keithschwarz.com/interesting/code/?dir=find-duplicate
'''
def findIntersection(arr):
    if len(arr) == 0 : return -1
    slow = 0
    fast = 0
    maxLoop = len(arr) * 2

    for i in xrange(0,maxLoop):
        slow = arr[slow]
        fast = arr[fast]
        fast = arr[fast]
        if slow == fast:
            break

    find = 0
    for i in xrange(0,maxLoop):
        slow = arr[slow]
        find = arr[find]
        if slow == find:
            return find
    return -1

arr = [1,2,4,4,3]
f = findIntersection(arr)
print f
