class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        right = len(nums) - 1
        lastVal = nums[right]
        targetIsOnLeft = (target > lastVal)
        
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            midVal = nums[mid]
            if midVal == target:
                return mid
            
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

        return -1
