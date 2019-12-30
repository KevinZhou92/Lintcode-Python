'''
=> DFS + Memorization
Time: O(n * m)
Space: O(n * m)
'''
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        '''
        if char equal, s1 + 1, s2 + 1
        if char not equal, 1 + res of s1 + 1, s2 + 1, # replace
                           1 + res of s1 + 1, s2      # delete
                           1 + res of s1, s2 + 1      # insert
        
        '''
        self.change_count = {}
        
        return self.dfs(word1, word2, 0, 0)
        
    def dfs(self, source, target, s_start, t_start):
        if (s_start, t_start) in self.change_count:
            return self.change_count[(s_start, t_start)]
        
        if s_start == len(source):
            return len(target) - t_start
        
        if t_start == len(target):
            return len(source) - s_start
            
        res = sys.maxsize
        if source[s_start] == target[t_start]:
            res = min(res, self.dfs(source, target, s_start + 1, t_start + 1))
        else:
            res = min(res, 1 + self.dfs(source, target, s_start + 1, t_start), 1 + self.dfs(source, target, s_start + 1, t_start + 1), 1 + self.dfs(source, target, s_start, t_start + 1))
        self.change_count[(s_start, t_start)] = res    
        
        return res