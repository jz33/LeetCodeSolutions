'''
85 Maximal Rectangle
https://oj.leetcode.com/problems/maximal-rectangle/
Inspired by "Largest Rectangle in Histogram"
'''
# O(n), use a stack
def largestRectangleInHistogram(ls):
    ls = [0] + ls + [0]
    stack = [0]
    maxArea = 0
    for i, v in enumerate(ls):
        while v < ls[stack[-1]]:
            h = ls[stack.pop()]
            maxArea = max(maxArea, (i-1-stack[-1])*h)
        stack.append(i)
    return maxArea

def largestRectangleInMatrix(mat,rowSize, colSize):
    ls = [0] * colSize
    maxArea = 0
    for i in range(0,rowSize):
        for j in range(0,colSize):
            ls[j] = 0 if mat[i][j] == '0' else ls[j] + 1
        maxArea = max(maxArea, largestRectangleInHistogram(ls))
    return maxArea

#API
def maximalRectangle(mat):
    rowSize = len(mat)
    if rowSize == 0: return 0
    colSize = len(mat[0])
    if colSize == 0: return 0
    return largestRectangleInMatrix(mat,rowSize,colSize)
        
def main():
    
    mat = [\
          '000100',\
          '011011',\
          '011111',\
          '111011',\
          '110111',\
          ]
    
    #mat = ['0']
    print maximalRectangle(mat)
    
if __name__ == "__main__":
    main()
