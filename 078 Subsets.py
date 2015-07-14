'''
Subsets
https://oj.leetcode.com/problems/subsets/
'''
def power(nums):
    if len(nums) == 0: return []
    
    nums.sort()
    pow_set_size = 1 << len(nums);
    ret = [[] for x in xrange(0,pow_set_size)];
    
    for counter in xrange(0,pow_set_size):
        buf = [];
        for j in xrange(0,len(nums)):
            if (counter & (1 << j)) != 0:
                buf.append(nums[j]);
        ret[counter] = buf
    return ret;
    
nums = []
print power(nums)
