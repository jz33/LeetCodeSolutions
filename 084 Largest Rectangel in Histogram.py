'''
84 Largest Rectangle in Histogram
https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
'''
# O(n^2), a normal approach
def largestRectangleArea(ls):
    curr = ls[0]
    maxArea = curr
    prev = curr
    for i in range(1,len(ls)):
        curr = ls[i]
        if curr == prev :
            continue
        lt = i - 1
        while lt > -1 and ls[lt] >= curr:
            lt -= 1
        rt = i + 1
        while rt < len(ls) and ls[rt] >= curr:
            rt += 1
        prev = curr
        maxArea = max((rt-lt-1)*curr,maxArea)
    return maxArea

# O(n), use a stack
def largestRectangleAreaStack(ls):
    ls = [0] + ls + [0]
    stack = [0]
    maxArea = 0
    for i, v in enumerate(ls):
        while v < ls[stack[-1]]:
            h = ls[stack.pop()]
            maxArea = max(maxArea, (i-1-stack[-1])*h)
        stack.append(i)
    return maxArea

def main():
    ls = [2,1,5,6,2,3]
    ls = [2,1,5,6,2,3,0]
    ls = [3,3,2,2]
    ls = [1,2,3,4]
    #ls = randInList(12,0,10)
    
    print ls
    print largestRectangleArea(ls)
    print largestRectangleAreaStack(ls)
        
if __name__ == "__main__":
    main()
