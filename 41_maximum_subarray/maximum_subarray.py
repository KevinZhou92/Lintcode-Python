"""
=> Greedy Solution
[−2,2,−3,4,−1,2,1,−5,3]
start for each number, expanding to right
if tmp_res + cur_num <= cur_num:
    tmp_res = cur_num
else:
    tmp_res += cur_num
res = max(res, tmp_num)

"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        
        res = nums[0]
        tmp_res = nums[0]
        for i in range(1, len(nums)):
            if tmp_res + nums[i] < nums[i]:
                tmp_res = nums[i]
            else:
                tmp_res += nums[i]
            res = max(res, tmp_res)
                    
        return res
    
"""
=> Prefix Sum
[−2,2,−3,4,−1,2,1,−5,3]
 -2,0,-3,1,0, 2,3,-2,1 

"""
class Solution2:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        res = nums[0]
        prefix_sum = nums[0]
        min_prefix = nums[0]
        for num in nums:
            prefix_sum += num
            res = max(res, prefix_sum - min_prefix)
            min_prefix = min(prefix_sum, min_prefix)
        
        return res