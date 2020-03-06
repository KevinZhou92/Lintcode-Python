class Solution:
    """
    @param X: a integer
    @param Y: a integer
    @param nums: a list of integer
    @return: return the maximum index of largest prefix
    """
    def LongestPrefix(self, X, Y, nums):
        # write your code here
        if not nums:
            return -1
            
        count_X = count_Y = 0
        res = -1
        for index in range(len(nums)):
            if nums[index] == X:
                count_X += 1
            if nums[index] == Y:
                count_Y += 1
            if count_X > 0 and count_X == count_Y:
                res = index
        
        return res
        
