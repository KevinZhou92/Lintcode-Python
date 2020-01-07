'''
=> Brute Force
Time: O(n^2)
Space: O(n)
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return [-1, -1]

        prefix_sums = [0] * (len(nums) + 1)
        tmp_sum = 0
        for i in range(1, len(nums) + 1):
            tmp_sum += nums[i - 1]
            prefix_sums[i] = tmp_sum
        
        min_sum = sys.maxsize
        res = []
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                if abs(prefix_sums[j] - prefix_sums[i]) < min_sum:
                    min_sum = abs(prefix_sums[j] - prefix_sums[i])
                    res = [i, j - 1]
                    
        return res