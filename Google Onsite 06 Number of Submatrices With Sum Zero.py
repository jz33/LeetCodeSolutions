'''
https://leetcode.com/discuss/interview-question/494524/Google-or-Onsite-or-Number-of-Submatrices-With-Sum-Zero

Given a matrix full of 0s and 1s, find the number of sub groups of zeroes.
Edit: You can also consider as number of rectangles formed by 0s.

[0,0,1,0,0] 
"""
# subgroups = 6 

pattern : count

0 : 4

00 : 2
"""
 
[ 
0,0,1,0,0
0,1,0,0,0
] 
"""
# subgroups = 17

pattern : count

0 : 8

00 : 4

000 : 1

0
0 : 3

00
00:1
"""
I tried using number of substrings formula, n*(n+1)/2. That is true only for 1 dimensional list.
There has to be some variation for the above. Any idea?

Related problems:

https://leetcode.com/discuss/interview-question/432092/
https://leetcode.com/discuss/interview-question/477890/
https://www.hackerrank.com/challenges/demidenko-farmer/editorial
'''
class Solution:
    def countAllZeroSubmatrices(self, mat: List[List[int]], target: int) -> int:
        '''
        Similar and simpler to 1074. Number of Submatrices That Sum to Target
        But this is O(n^3)
        '''
        rowCount = len(mat)
        colCount = len(mat[0])
        res = 0
        
        # There are 2 iteration on rowCount. Ideally, should iterate rowCount
        # or colCount whoever is smaller
        for i in range(rowCount):
            # Use a sum array to record previous row results
            arr = [0] * colCount
            for k in range(i, rowCount):
                # starting column index on arr that arr[left] is 0
                left = 0
                for c in range(colCount):
                    arr[c] += mat[k][c]
                    if arr[c] == 0:
                        res += c - left + 1
                    else:
                        left = c + 1
        
        return res
       
class Solution:
    def countHisto(self, srcHeights: List[int]) -> int:
        heights = srcHeights + [0]
        stack = [] # [height index]
        count = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                j = stack.pop()
                ph = heights[j]
                
                # So how many new rectangles?
                # Clearly, new rectangles should all include j column.
                # Then from j, expand to left, till stack[-1], there are "left" choices
                # From j to right till i there are "right" choices.
                # Then rectangle count is left * right
                left = j - stack[-1] if stack else j + 1
                right = i - j
                count += ph * left * right
            stack.append(i)
        return count
    
    def countAllZeroSubmatrices(self, mat: List[List[int]], target: int) -> int:
        '''
        Use 85 Maximal Rectangle, O(n^2)
        '''
        rowCount = len(mat)
        colCount = len(mat[0])
        res = 0

        heights = [0] * colCount
        for i in range(rowCount):
            for c in range(colCount):
                if mat[i][c] == 0:
                    heights[c] += 1
                else:
                    heights[c] = 0
            res += self.countHisto(heights)  
        return res
