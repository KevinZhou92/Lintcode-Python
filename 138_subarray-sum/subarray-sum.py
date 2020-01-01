class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        
        # [-3, 1, 2, -3, 4]
        # -3 -2  0  -3   1

        sum_indices = {}
        sum_indices[0] = -1
        sums = 0
        res = []
        for index in range(len(nums)):
            sums += nums[index]
            if sums in sum_indices:
                res.append(sum_indices[sums] + 1)
                res.append(index)
                break
            sum_indices[sums] = index
            
        return res