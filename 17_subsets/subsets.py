'''
=> DFS
Time: O(n*2^n)
The number of recursive calls, T(n) satisfies the recurrence T(n) = T(n - 1) + T(n - 2) + ... + T(1) + T(0), which solves to T(n) = O(2^n). Since we spend O(n) time within a call, the time complexity is O(n2^n)
'''
import copy
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return[[]]
        
        nums.sort()
        self.res = [[]]
        self.dfs(nums, 0, [])
        
        return self.res        
    
    def dfs(self, nums, start, tmp):
        if len(tmp) == len(nums):
            return
            
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.res.append(copy.copy(tmp))
            self.dfs(nums, i + 1, tmp)
            tmp.pop()

