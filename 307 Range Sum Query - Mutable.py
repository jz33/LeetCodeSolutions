'''
307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''
class NumArray:
    '''
    Segment Tree
    '''
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.tree = []
        if self.length:
            self.buildTree(nums)

    def buildTree(self, nums: List[int]):
        # The sizeo of segment tree is double length - 1
        # For example, array [8,9,2,4,5,7]
        # Tree is:
        # [35,18,17,6,12,8,9,2,4,5,7]
        #          35
        #       /      \
        #      18      17
        #    /    \    / \
        #   6     12  8   9
        #  / \    / \
        # 2   4  5   7
        length = len(nums)
        tree = [None] * (length * 2 - 1);
        
        # Build leaves
        for i, e in enumerate(nums):
            tree[getLeafIndex(i, length)] = e
        
        # Build inners
        for i in range(length-2, -1, -1):
            tree[i] = tree[getLeft(i)] + tree[getRight(i)]

        self.tree = tree

    def update(self, i: int, val: int) -> None:
        tree = self.tree
        length = self.length

        # Update leaf
        leaveIndex = getLeafIndex(i, length)
        if tree[leaveIndex] == val:
            return

        tree[leaveIndex] = val

        # Update parents
        i = leaveIndex
        while i != 0:
            p = getParent(i)
            tree[p] = tree[getLeft(p)] + tree[getRight(p)]
            i = p
        
    def sumRange(self, left: int, right: int) -> int:
        tree = self.tree
        length = self.length

        left = getLeafIndex(left, length)
        right = getLeafIndex(right, length)
        sum = 0

        # From the 2 leaves, go up
        while left <= right:
            if left == right:
                sum += tree[left]
                break

            # Add to sum if left is on right of its parent
            # Or right is on left of its parent
            if isRightChild(left):
                sum += tree[left]
                left += 1
            if isLeftChild(right):
                sum += tree[right]
                right -= 1

            left = getParent(left)
            right = getParent(right)

        return sum

# Getting indexed part is same as heap implementation
def getLeft(i):
    '''
    Index of left child
    '''
    return (i << 1) + 1

def getRight(i):
    '''
    Index of right child
    '''
    return (i + 1) << 1

def getParent(i):
    '''
    Index of parent
    Root or less then 0 will return itself
    '''
    return (i - 1) >> 1 if i > 0 else i

def isLeftChild(i):
    '''
    Whether i is left child of its parent node, i.e,
    i should be odd
    '''
    return (i & 1) == 1

def isRightChild(i):
    '''
    Whether i is right child of its parent node, i.e,
    i should be even
    '''
    return (i & 1) == 0

def getLeafIndex(i, length):
    '''
    Array index => Tree leave node index
    '''
    return length - 1 + i



class NumArray:
    '''
    Binary Indexed Tree
    '''
    def __init__(self, nums: List[int]):
        self.nums = [0] * len(nums)
        self.bits = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])
        
    def update(self, i: int, val: int):
        diff = val - self.nums[i]
        if diff != 0:
            self.nums[i] = val
            
            i += 1 # no need to update bits[0]
            while i <= len(self.nums):
                # This is essential from leaf to parents
                self.bits[i] += diff
                i += (i & -i)
                        
    def sumRange(self, i: int, j: int) -> int:
        return self.getSum(j+1) - self.getSum(i)

    def getSum(self, i: int) -> int:       
        # Get sum before index i
        # This is from parents to leaf
        total = 0
        while i > 0: # bits[i] is 0, no need
            total += self.bits[i]
            i -= (i & -i)
        return total
