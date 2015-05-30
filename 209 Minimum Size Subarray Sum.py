'''
209 Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
'''
def minSubarraySum(arr,tag):
    # find first sum
    s = 0
    i = 0
    while i< len(arr):
        s += arr[i]
        if s >= tag: break
        i += 1
    
    # not found    
    if i == len(arr): return

    j = 0 # left
    minLen = i + 1
    
    while i< len(arr):
        # try shrink
        while s >= tag:
            s -= arr[j]
            j += 1
            
        # update
        minLen = min(minLen,i - j + 2)
        
        # extand
        i += 1
        while i < len(arr):
            s += arr[i]
            if s >= tag: break
            i += 1
        
    print "left index : {}, right index : {}, minLen: {}".format(j-1,i-1,minLen)
        
def main():
    arr = [2,3,1,2,4,3]
    tag = 7
    minSubarraySum(arr,7)

if __name__ == '__main__':
    main()  
