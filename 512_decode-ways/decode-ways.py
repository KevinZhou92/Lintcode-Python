'''
=> DFS + Memorization
Time: O(n)
Space: O(n)
'''
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        self.res_map = {}
        
        return self.dfs(s, 0)
    
    def dfs(self, string, start):
        res = 0
        if start in self.res_map:
            return self.res_map[start]
            
        if start == len(string):
            return 1
            
        if string[start] == '0':
            self.res_map[start] = 0
            return res
        
        for i in range(2):
            if start + i + 1 <= len(string) and 0 < int(string[start: start + i + 1]) <= 26:
                res += self.dfs(string, start + i + 1)
                
        self.res_map[start] = res
        
        return res

'''
=> DP
Time: O(n)
'''
class Solution2:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        
        string_len = len(s)
        dp = [0] * (string_len + 1)
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
                
            if i > 1:
                num = ord(s[i - 1]) - ord('0') + (ord(s[i - 2]) - ord('0')) * 10
                if 10 <= num <= 26:
                    dp[i] += dp[i - 2]
                    
        return dp[string_len]
        
                