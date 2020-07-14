class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        # Make sure left most != right most
        # This is the only difference of Search in Rotated Sorted Array II to Search in Rotated Sorted Array I
        right = len(nums) - 1
        while right > 0 and nums[right] == nums[0]:
            if nums[right] == target:
                return True
            right -= 1
        lastVal = nums[right]
        
        targetIsOnLeft = (target > lastVal)
        
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            midVal = nums[mid]
            if midVal == target:
                return True
            ,
            # The trick is here
            midValIsOnLeft = midVal > lastVal
            if targetIsOnLeft and not midValIsOnLeft:
                midVal = float('inf')
            elif not targetIsOnLeft and midValIsOnLeft:
                midVal = float('-inf')

            # Regular binary search afterwards
            if midVal < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
