'''
=> DFS 

Time: O(n^2)
Space: O(n)
'''
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict:
            return not dict and not s
        
        dict = set(dict)
        return self.dfs(s, 0, dict)
        
    def dfs(self, string, startIndex, wordSet):
        if startIndex == len(string):
            return True
            
        res = False
        for index in range(startIndex, len(string)):
            curWord = string[startIndex: index + 1]
            if curWord not in wordSet:
                continue
            res |= self.dfs(string, index + 1, wordSet)
        
        return res