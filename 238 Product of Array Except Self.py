'''
Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
'''
def productExceptSelf(nums):
    if len(nums) < 2: return nums
    
    ret = [0 for i in xrange(len(nums))]

    '''
    From left to right, construct left-prodcut
    array, i.e., ret[i] = product(nums[0]...nums[i])
    '''
    ret[0] = nums[0]
    for i in xrange(1,len(nums)-1):
        ret[i] = nums[i] * ret[i-1]

    # The right product beyond current index
    rt = 1

    '''
    From right to left, ret[i] = left * right
    '''
    for i in xrange(len(nums) - 1, 0, -1):
        ret[i] = ret[i-1] * rt
        rt *= nums[i]
    ret[0] = rt   

    return ret
 
        
nums = [1,2,3,4]
print productExceptSelf(nums)
