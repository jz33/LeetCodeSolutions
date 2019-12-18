'''
835. Image Overlap
https://leetcode.com/problems/image-overlap/

Two images A and B are given, represented as binary, square matrices of the same size.
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units),
and place it on top of the other image.  After, the overlap of this translation is the number of positions that
have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
'''
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A)
        pointsA = []
        pointsB = []
        for i in range(size):
            for j in range(size):
                if A[i][j] == 1:
                    pointsA.append((i,j))
                if B[i][j] == 1:
                    pointsB.append((i,j))
        
        # Compute histogram of distances.
        # If point pairs are in same distances, they can be
        # overlapped together after sliding
        distances = collections.Counter()
        for a in pointsA:
            for b in pointsB:
                d = (a[0] - b[0], a[1] - b[1])
                distances[d] += 1

        return distances.most_common(1)[0][1] if distances else 0
