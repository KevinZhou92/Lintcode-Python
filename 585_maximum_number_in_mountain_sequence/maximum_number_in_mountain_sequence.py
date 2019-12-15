'''
O(n) Solution: iterate through, find the maximum
'''
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
            
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
                
        if nums[start] < nums[end]:
            return nums[end]
        
        return nums[start]
            
            