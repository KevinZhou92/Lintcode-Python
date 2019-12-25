'''
=> DP
Time: O(n^2)
Space: O(n) 
'''
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
            
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
