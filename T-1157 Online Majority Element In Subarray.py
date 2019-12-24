'''
1157. Online Majority Element In Subarray
https://leetcode.com/problems/online-majority-element-in-subarray/

Implementing the class MajorityChecker, which has the following API:

MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
int query(int left, int right, int threshold) has arguments such that:
0 <= left <= right < arr.length representing a subarray of arr;
2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs
at least threshold times, or -1 if no such element exists.

Example:

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
'''
from random import randint
from collections import defaultdict

def binary_left(arr, target):
    '''
    Equivalent to bisect_left
    '''
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

def binary_right(arr, target):
    '''
    Equivalent to bisect_right
    '''
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class MajorityChecker:
    def __init__(self, arr: List[int]):
        book = defaultdict(list)
        for i, e in enumerate(arr):
            book[e].append(i)
        self.book = book
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        '''
        Random pick an element in range and there is 50% chance 
        this is a majority element
        '''
        for _ in range(10):
            test = self.arr[randint(left, right)]
            indexes = self.book[test]
            leftBound = binary_left(indexes, left)
            rightBound = binary_right(indexes, right)
            if rightBound - leftBound >= threshold:
                return test
        return -1        

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
