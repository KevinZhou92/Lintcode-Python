class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        rob_first = [0] * len(nums)
        rob_first[0] = 0
        rob_first[1] = nums[0]
        for i in range(2, len(nums)):
            rob_first[i] = max(rob_first[i - 2] + nums[i - 1], rob_first[i - 1])
            
        rob_last = [0] * len(nums)
        rob_last[0] = 0
        rob_last[1] = nums[1]
        for i in range(2, len(nums)):
            rob_last[i] = max(rob_last[i - 2] + nums[i], rob_last[i - 1])
            
        return max(max(rob_first), max(rob_last))
        