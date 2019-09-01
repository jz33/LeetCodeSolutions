'''
217 Contains Duplicate
219 Contains Duplicate II
220 Contains Duplicate III
https://leetcode.com/problems/contains-duplicate/
https://leetcode.com/problems/contains-duplicate-ii/
https://leetcode.com/problems/contains-duplicate-iii/
'''
# 217
def containsDuplicate(nums):
    return len(nums) > len(set(nums))       

# 219
def containsDuplicate2(nums,k):
    ref = set()
    for i,v in enumerate(nums):
        if i > k: 
            ref.remove(nums[i-k-1])
        if v in ref: return True
        else: ref.add(v)
    return False

'''
220
https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation
Assume all numbers are >= 0

k: difference of i,j
t: distance of nums[i],nums[j]
'''
def containsDuplicate3(nums,k,t):
    if k < 1 or t < 0: return False
    
    # bucket (integer): value(integer)
    # bucket = v / (t+1)
    buckets = {}
    for i,v in enumerate(nums):
        if i > k:
            b = nums[i-k-1] // (t+1);
            del buckets[b]

        b = v // (t+1);

        # When convert value to bucket, only current, -1, +1 need to look
        # Otherwise we need to look next k values
        if b in buckets or \
            b-1 in buckets and v - buckets[b-1] <= t or \
            b+1 in buckets and buckets[b+1] - v <= t:
            return True

        buckets[b] = v  
    return False
    
def main():
    arr = [4,2]
    print containsDuplicate3(arr,2,1)
    
if __name__ == '__main__':
    main()
