class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
                
        if nums[end] == target:
            return end
            
        if nums[start] == target:
            return start
            
        return -1

# Time: O(logN)
# Space: O(1)