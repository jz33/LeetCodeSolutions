'''
209 Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
'''
def minSubarraySum(arr,bar):
    rt = 0
    sum = 0
    
    # first sum
    while rt < len(arr):
        sum += arr[rt]
        rt += 1
        if sum >= bar: break
    
    if sum < bar: return 0
    
    lt = 0
    minRange = rt
    
    while rt < len(arr):
        # add one
        if sum < bar:
            sum += arr[rt]
            rt += 1
        # shrink one
        else:
            minRange = min(minRange,rt-lt)
            sum -= arr[lt]
            lt += 1
    
    # shrink to end
    while lt < len(arr) and sum >= bar:
        minRange = min(minRange,rt - lt)
        sum -= arr[lt]
        lt += 1

    return minRange        

arr = [2,3,1,2,4,3]
bar = 7
print minSubarraySum(arr,bar)
