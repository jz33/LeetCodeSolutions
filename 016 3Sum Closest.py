'''
3Sum Closest
https://leetcode.com/problems/3sum-closest/
'''

def threeSumClosest(nums, target):
    if len(nums) < 3: return 0   
    nums.sort()

    minDiff = target - (nums[0] + nums[1] + nums[2]);
    if minDiff == 0: return target
        
    for i in xrange(0,len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            diff = target - (nums[i] + nums[j] + nums[k]);
            if diff == 0:
                return target;
            
            minDiff = minDiff if abs(minDiff) <= abs(diff) else diff
            
            if diff > 0:      
                j += 1
                while j + 1 < k and nums[j] == nums[j+1]: j += 1
            else:
                k -= 1
                while k - 1 > j and nums[k] == nums[k-1]: k -= 1
                
        while i + 1 != len(nums) - 2 and nums[i+1] == nums[i] : i += 1
    
    return target - minDiff;

nums = [-1,2,1,4]
target = 1

print threeSumClosest(nums, target)
