'''
493. Reverse Pairs
https://leetcode.com/problems/reverse-pairs/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
'''
class SegmentTree:
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
        tree = [None] * (self.length * 2 - 1);
        
        # Build leaves
        for i, e in enumerate(nums):
            tree[self.getLeaf(i)] = e
        
        # Build inners
        for i in range(self.length - 2, -1, -1):
            tree[i] = tree[self.getLeft(i)] + tree[self.getRight(i)]

        self.tree = tree

    def increase(self, i: int, val: int):
        leafIndex = self.getLeaf(i)
        leafValue = self.tree[leafIndex] 
        self.update(i, leafValue + val)
        
    def update(self, i: int, val: int):
        tree = self.tree

        # Update leaf
        leafIndex = self.getLeaf(i)
        if tree[leafIndex] == val:
            return

        tree[leafIndex] = val

        # Update parents
        i = leafIndex
        while i != 0:
            p = self.getParent(i)
            tree[p] = tree[self.getLeft(p)] + tree[self.getRight(p)]
            i = p
        
    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return 0
        
        tree = self.tree

        left = self.getLeaf(left)
        right = self.getLeaf(right)
        leavesSum = 0

        # From the 2 leaves, go up
        while left <= right:
            if left == right:
                leavesSum += tree[left]
                break

            # Add to sum if left is on right of its parent
            # Or right is on left of its parent
            if self.isRightChild(left):
                leavesSum += tree[left]
                left += 1
    
            if self.isLeftChild(right):
                leavesSum += tree[right]
                right -= 1

            left = self.getParent(left)
            right = self.getParent(right)

        return leavesSum

    # Index helpers
    def getLeft(self, i):
        '''
        Get left child index of i
        '''
        return (i << 1) + 1

    def getRight(self, i):
        '''
        Get right child index of i
        '''
        return (i + 1) << 1

    def getParent(self, i):
        '''
        Get parent index of i
        If i is root or less then 0, return i
        '''
        return ((i - 1) >> 1) if i > 0 else i

    def isLeftChild(self, i):
        '''
        Whether i is left child of its parent node
        '''
        return (i & 1) == 1

    def isRightChild(self, i):
        '''
        Whether i is right child of its parent node
        '''
        return (i & 1) == 0

    def getLeaf(self, i):
        '''
        The i is original array index, get its leaf node index
        '''
        return self.length - 1 + i
    
class Solution:
    def reversePairs(self, nums: List[int]) -> int:        
        # Distinct nums
        distincts = list(sorted(set(nums)))
        
        def getRightBound(e : int) -> int:
            '''
            Get the largest index from distincts which
            meet this questions requirement
            Using binary search
            '''
            left = 0
            right = len(distincts) - 1
            
            while left <= right:
                mid = left + ((right - left) >> 1)
                if distincts[mid] * 2 < e:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # right can be -1
            # Since left > right now, left must be invalid
            return right 
        
        valueToIndex = {v : i for i, v in enumerate(distincts)}
        
        # Segment tree is used for count only
        tree = SegmentTree([0] * len(distincts))        
        res = 0
        for i in range(len(nums)-1, -1, -1):
            e = nums[i]
            j = getRightBound(e) 
            if j >= 0:
                res += tree.sumRange(0, j)
            tree.increase(valueToIndex[e], 1)
        return res
