"""
=> DFS
[-1,4,-2,3,-2,3], k = 2, res = 8
4 + (3 + -2 + 3)
0, 0

prepare an 2-d array sum[i][j], store the sum from i to j
dfs on this array, every time pick an non-overlapping area, add the value
and return

dfs(nums, sum_array, k, remains, cur_sum)
"""
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        if not nums or k < 0 or k > len(nums):
            return 0
            
        sum_array = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            if i > 0:
                sum_array[0][i] += sum_array[0][i - 1]
            sum_array[0][i] += nums[i]
            for j in range(1, i + 1):
                sum_array[j][i] = sum_array[0][i] - sum_array[0][j - 1]
        
        self.result_map = {}
        print(sum_array)
        res = self.dfs(nums, sum_array, k, k, 0, 0)
        
        return res
    
    def dfs(self, nums, sum_array, k, remains, start_index, cur_sum):
        if remains == 0:
            return cur_sum
        
        if remains > len(nums) - start_index:
            return -sys.maxsize
        
        res = -sys.maxsize
        for i in range(start_index, len(nums) - remains + 1):
            for j in range(start_index, i + 1):
                cur_sum += sum_array[j][i]
                res = max(res, self.dfs(nums, sum_array, k, remains - 1, i + 1, cur_sum))
                cur_sum -= sum_array[j][i]
            
        return res
        
"""
DFS Top-Down
every time, calculate an interval with maximum sum, and dfs for rest k - 1
use memorization to reduce time

dfs(nums, k, start_index, cur_sum)

            [-4,5,-4,5]
local_min    -4,-4
local_max    -4 5
"""
class Solution2:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        if k > len(nums) or k <= 0 or not nums:
            return 0
        
        self.sum_map = {}
        res = self.dfs(nums, k, 0)
        print(self.sum_map)
        return res 
        
    def dfs(self, nums, count, start_index):
        if (start_index, count) in self.sum_map:
            return self.sum_map[(start_index, count)]
            
        if count > len(nums) - start_index:
            return -sys.maxsize
            
        if count == 0:
            return 0
            
        res = -sys.maxsize
        tmp_res = -sys.maxsize
        local_sum = 0
        for i in range(start_index, len(nums)):
            if local_sum + nums[i] <= nums[i]:
                local_sum = nums[i]
            else:
                local_sum += nums[i]
            
            tmp_res = self.dfs(nums, count - 1, i + 1)
            res = max(res, tmp_res + local_sum)
            
        self.sum_map[(start_index, count)] = res
        return res       

class WrongSolution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        if k > len(nums) or k <= 0 or not nums:
            return 0
        
        self.sum_map = {}
        res = self.dfs(nums, k, 0, 0)
        
        return res 
        
    def dfs(self, nums, count, start_index, cur_sum):
        if (start_index, count) in self.sum_map:
            return self.sum_map[(start_index, count)]
            
        if count > len(nums) - start_index:
            return -sys.maxsize
            
        if count == 0:
            return cur_sum
            
        res = -sys.maxsize
        tmp_res = -sys.maxsize
        local_sum = 0
        for i in range(start_index, len(nums)):
            if local_sum + nums[i] <= nums[i]:
                local_sum = nums[i]
            else:
                local_sum += nums[i]
            
            # this step is wrong, for example, [-7,1,-1,-3,-4,-10,2,-100,-51,-12]
            # notice dfs always search along a path until not available
            # assume we need to pick 4 subarray, the dfs search will get result for start_index = 4,
            # count = 1 as -7, the execution is like
            # start_index count picked cur_sum
            #  0           4     -7      -7
            #  1           3     1       -6
            # loop within start_index = 2, count = 2
            #  2           2     -1      -7
            #  3           2     -3      -9
            #  4           1     2       -7
            # so the maximum value for start_index = 7, count = 2 is -7, which is wrong, the correct value should be 2.
            # when we write dfs search to find optimum value for a subproblem, we should not pass in 
            # a value from a bigger state, instead, we should use a bottom-up solution
            

            tmp_res = self.dfs(nums, count - 1, i + 1, cur_sum + local_sum)
            res = max(res, tmp_res)
            
        self.sum_map[(start_index, count)] = res
        
        return res