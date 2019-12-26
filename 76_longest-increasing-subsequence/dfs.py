
'''
=> DFS + Memorization
Time: O(n^2) 
'''
class Solution2:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
            
        self.res = 0 
        self.res_map = {}
        self.dfs(nums, len(nums))
        
        return self.res
        
    def dfs(self, nums, n):
        if n <= 1:
            return 1
        
        if n in self.res_map:
            return self.res_map[n]
        
        cur_max = 1
        for i in range(1, n):
            # from 1, 2, to n - 1
            tmp_res = self.dfs(nums, i)
            if nums[i - 1] < nums[n - 1] and tmp_res + 1 > cur_max:
                cur_max = tmp_res + 1
            # from n - 1, n - 2, to n
            # tmp_res = self.dfs(nums, n - i)
            # if nums[n - i - 1] < nums[n - 1] and tmp_res + 1 > cur_max:
            #     cur_max = tmp_res + 1
            
            self.res = max(self.res, cur_max)
        
        self.res_map[n] = cur_max
        return cur_max