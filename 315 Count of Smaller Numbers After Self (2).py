'''
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
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
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Utilize Segment Tree
              
        # Build sorted element : index array.
        # These sorted element will be tree leaves.
        book = {v: i for i, v in enumerate(sorted(set(nums)))}
        
        # Leaf values are the count of each element.
        tree = SegmentTree([0] * len(book))
        
        size = len(nums)
        res = [0] * size

        for i in range(size-1, -1, -1):
            e = nums[i]
            j = book[e]
            
            # The count of smaller elements after e is
            # the tree's count of elements who are smaller than e
            # Because element counts are added from back,
            # current count represents after element information
            res[i] = tree.sumRange(0, j-1)
            
            # Increase element count to tree
            tree.increase(j, 1)
        
        return res        
