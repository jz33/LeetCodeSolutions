'''
152 Maximum Product Subarray
https://oj.leetcode.com/problems/maximum-product-subarray/
''' 
def func3(f,a,b,c):
    return f(a,f(b,c))
    
def maxProduct(ls):
    if len(ls) == 0: return 0

    ret = ls[0]
    maxVal = ls[0]
    minVal = ls[0]
    
    for i in xrange(1,len(ls)):
        v = ls[i]
        prev_maxVal = maxVal
        
        maxVal = func3(max, v, v * maxVal, v * minVal)
        minVal = func3(min, v, v * prev_maxVal, v * minVal)
        
        ret = max(ret,maxVal);
    return ret

def simple_test(func):
    ls = [-2,0,-1]
    print func(ls)
    ls = [2,3,-2,4]
    print func(ls)
    ls = [2,3,0,-4,2,-2]
    print func(ls)
    
simple_test(maxProduct)
