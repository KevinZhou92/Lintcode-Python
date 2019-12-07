"""
=> DP
n = 3
1, 1, 1
1, 2
2, 1
"""

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if not n:
            return 0
            
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

"""
=> DFS + Memorization
"""
class Solution2:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if not n:
            return 0
            
        return self.dfs(n, {})
    
    def dfs(self, n, climbs):
        if n in climbs:
            return climbs[n]
            
        if n <= 1:
            return 1
            
        res = self.dfs(n - 1, climbs) + self.dfs(n - 2, climbs)
        climbs[n] = res
        
        return res