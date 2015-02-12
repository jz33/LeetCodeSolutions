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
            ls[j] = 0 if mat[i][j] == 0 else ls[j] + 1
        maxArea = max(maxArea, largestRectangleInHistogram(ls))
    return maxArea

def main():
    mat = [
          [0,0,0,1,0,0],
          [0,1,1,0,1,1],
          [0,1,1,1,1,1],
          [1,1,1,0,1,1],
          [1,1,0,1,1,1],
          ]

    print largestRectangleInMatrix(mat,5,6)
    
if __name__ == "__main__":
    main()
