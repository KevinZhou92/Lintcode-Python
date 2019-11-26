import copy
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    
    """
    [DFS]
    1 2 2 
    # #
        
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        
        nums.sort() 
        self.res = []
        self.visited = [False for _ in nums]
        self.dfs(nums, [])
        
        return self.res
        
    def dfs(self, nums, cur_list):
        if len(cur_list) == len(nums):
            self.res.append(cur_list)
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not self.visited[i - 1]:
                continue
            if not self.visited[i]:
                self.visited[i] = True
                cur_list.append(nums[i])
                self.dfs(nums, copy.copy(cur_list))
                cur_list.pop()
                self.visited[i] = False
    """    
    [BFS]
    1 2 2 
    # #

    The trick is to put remainning elements with current value in to the queue,
    when adding next elements to the queue, we make sure that we don't add duplicate
    element to the same position
    """        

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        nums.sort()
        res = []
        queue = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            queue.append([[nums[i]], nums[:i] + nums[i + 1:]])
            
        deque = collections.deque(queue)
       
        while deque:
            cur_list, available_nums = deque.popleft()
            if len(cur_list) == len(nums):
                res.append(cur_list)
                continue
            for i in range(len(available_nums)):
                if i > 0 and available_nums[i] == available_nums[i - 1]:
                    continue
                cur_list.append(available_nums[i])
                deque.append([copy.copy(cur_list), available_nums[:i] + available_nums[i + 1:]])
                cur_list.pop()
                
        return res