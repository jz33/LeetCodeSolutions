'''
1570. Dot Product of Two Sparse Vectors
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

    SparseVector(nums) Initializes the object with the vector nums
    dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values,
you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:
    n == nums1.length == nums2.length
    1 <= n <= 10^5
    0 <= nums1[i], nums2[i] <= 100
'''
class SparseVector:
    def __init__(self, nums: List[int]):
        # [(index, value)]
        self.data = [(index, value) for index, value in enumerate(nums) if value != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, that: 'SparseVector') -> int:
        result = 0
        si = 0 # pointer for self
        ti = 0 # pointer for that
        while si < len(self.data) and ti < len(that.data):
            sj, sv = self.data[si]
            tj, tv = that.data[ti]
            if sj == tj:
                result += sv * tv
                si += 1
                ti += 1
            elif sj < tj:
                si += 1
            else:
                ti += 1
        return result
    
'''
Facebook interview:
coding2：变体 义务欺凌， 不要被原题给干扰，因为大哥要求是input直接给两个，每个都特别大，more than a million elements,
然后问怎么生成结果，我一开始跑偏了就是按照原题走的，后来大哥很友善的给我提醒
我七拐八拐的走到了可以chunk processing，但不是大哥想要的，‍‍‌‌‍‌‌‍‍‌‌‌‍‍‌‍‍他最终想要的是双指针，iterate
遇到两个都数字在计算。最后是写出来了但是完全没有底了，估计是挂或者weak hire
https://www.1point3acres.com/bbs/thread-1046761-1-1.html
'''
