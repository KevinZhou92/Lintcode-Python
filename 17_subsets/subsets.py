'''
=> DFS
[1,2,3]
start from each position
add cur subset and keep searching
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
            