"""
two non-overlapping subarrays have largest sum
[1, 3, -1, 2, -1, 2]
left to right 1  4   4(3)  5  5(4)  6
right to left       4(3)   3  2(1)  2
[1, 3] and [2, -1, 2] 
[1, 3, -1, 2] and [2].
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here 
        
        if not nums or len(nums) == 1:
            return 0
            
        
        prefix_max = [0 for i in range(len(nums))]
        max_sum = -sys.maxsize
        sum_value = 0
        for i in range(len(nums)):
            if sum_value + nums[i] < nums[i]:
                sum_value = nums[i]
            else:
                sum_value += nums[i]
            max_sum = max(max_sum, sum_value)
            prefix_max[i] = max_sum
        
        max_sum = -sys.maxsize
        sum_value = 0
        res = -sys.maxsize
        for i in range(len(nums) - 1, 0, -1):
            if sum_value + nums[i] < nums[i]:
                sum_value = nums[i]
            else:
                sum_value += nums[i]
            max_sum = max(max_sum, sum_value)
            res = max(res, max_sum + prefix_max[i - 1])
            
        return res