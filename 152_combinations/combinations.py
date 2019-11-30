"""
- DFS
n = 3, k = 2
everytime put a new number in to list, and next time search in [num + 1, n]
for num in (start, n + 1):
    search
return all
"""
import copy
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    
    def combine(self, n, k):
        # write your code here
        
        self.res = []
        self.dfs(1, n, k, [])
        
        return self.res
        
    def dfs(self, start_num, n, target_len, num_list):
         # Optimization: if available numbers is less than required
         # terminate current loop
         if n - start_num + 1 < target_len - len(num_list):
            return

        if len(num_list) == target_len:
            self.res.append(copy.copy(num_list))
            return 
        
        for num in range(start_num, n + 1):
            num_list.append(num)
            self.dfs(num + 1, n, target_len, num_list)
            num_list.pop()
            

"""
- BFS
"""
import copy
from collections import deque
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        
        queue = deque()
        
        for i in range(1, n - k + 2):
            queue.append([i])
            
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                cur_list = queue.popleft()
                if len(cur_list) == k:
                    res.append(cur_list)
                    continue
                for num in range(cur_list[-1] + 1, n + 1):
                    cur_list.append(num)
                    queue.append(copy.copy(cur_list))
                    cur_list.pop()
                    
                    
        return res
            
