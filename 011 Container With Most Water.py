import random
'''
11 Container With Most Water
https://oj.leetcode.com/problems/container-with-most-water/
http://yucoding.blogspot.com/2012/12/leetcode-question-22-container-with.html
'''
# generate a random int array with limits [a,b]
def createRandList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A

def maxRectangleArea(heights):
    maxArea = 0
    l = 0
    r = len(heights)-1
    if l == r : return 0
    
    while l < r:
        maxArea = max(abs(l-r)*min(heights[l],heights[r]),maxArea)
        if(heights[l]<=heights[r]): l += 1
        else : r -= 1
    return maxArea
    
def main():
    repeat = 1
    for i in range(repeat):
        n = i+5
        heights = createRandList(n,1,(i+n)*2)
        print heights
        print maxRectangleArea(heights)

if __name__ == "__main__":
    main()
