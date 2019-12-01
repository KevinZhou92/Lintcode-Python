import copy

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    
    """
    1 2 3
    
    """

    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
        
        nums.sort()       
        self.res = []
        self.visited = [0 for i in nums]
        self.dfs(nums, [])
        
        return self.res
        
    def dfs(self, nums, cur_res):
        if len(cur_res) == len(nums):
            self.res.append(copy.copy(cur_res))
            return
        
        for i in range(len(nums)):
            if self.visited[i] == 0:
                self.visited[i] = 1
                cur_res.append(nums[i])
                self.dfs(nums, cur_res)
                cur_res.pop()
                self.visited[i] = 0

class Solution2:   
    """
    [non-recursive]
    1 2 3
    + queue
    [[1] [2] [3]]
    
    """
    def permute(self, nums):
        # write your code here
        res = []
        if not nums:
            res.append([])
            return res
            
        queue = []
        nums.sort()
        for num in nums:
            queue.append([num])
            
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_list = queue.pop()
                if len(cur_list) == len(nums): 
                    res.append(cur_list)
                    continue
                for num in nums:
                    if num not in cur_list:
                        cur_list.append(num)
                        queue.append(copy.copy(cur_list))
                        cur_list.pop()
                        
        return res