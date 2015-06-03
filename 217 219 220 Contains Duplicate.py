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
def containsDuplicate2(nums,dist):
    ref = set()
    for i,v in enumerate(nums):
        if i > dist: 
            ref.remove(nums[i-dist-1])
        if v in ref: return True
        else: ref.add(v)
    return False

'''
220
https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation
Assume all numbers are >= 0
'''
def containsDuplicate3(nums,dist,diff):
    if dist < 1 or diff < 0: return False
    
    buckets = {} # bucket : value
    for i,v in enumerate(nums):
        if i > dist:
            b = nums[i-dist-1] / (diff+1); 
            del buckets[b]
            
        b = v / (diff+1);
        if b in buckets or \
            b-1 in buckets and v - buckets[b-1] <= diff or \
            b+1 in buckets and buckets[b+1] - v >= diff:
            return True
            
        buckets[b] = v  
    return False
    
def main():
    arr = [0,1,2,3,4,5,0,1,2,3,4,5]
    print containsDuplicate(arr)
    print containsDuplicate2(arr,5)
    print containsDuplicate2(arr,6)
    
    arr = [0,100,200,3,300,400,6,500,600,9]
    print containsDuplicate3(arr,2,3)
    print containsDuplicate3(arr,3,3)
    
if __name__ == '__main__':
    main()
