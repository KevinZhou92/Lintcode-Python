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
        for i in range(1, len(nums) + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        
        num_pairs = []
        for index, value in enumerate(prefix_sums):
            num_pairs.append((value, index))
        
        # 0 [-3, 1, 1, -3, 5]
        #    -3  -2 -1  -4, 1
        #  0  1   2  3   4
        num_pairs.sort(key=lambda x: x[0])
        res = []
        for i in range(len(num_pairs) - 1):
            if not res or abs(prefix_sums[res[1] + 1] - prefix_sums[res[0]]) > abs(num_pairs[i][0] - num_pairs[i + 1][0]):
                res = sorted([num_pairs[i][1] , num_pairs[i + 1][1]])
                res[1] -= 1
                
        return sorted(res)