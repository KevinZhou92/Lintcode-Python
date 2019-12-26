'''
=> DP
While painting ith fence, we have two options:
1. use the same color of previous wall, then we need to use different color of the one before previous one,
so it will be (k - 1) * preprevious one
2. use a different color than previous one, then we will have (k - 1) * previous one combinations
Add them up and move forward
'''
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        dp = [0, k, k * k, 0]
        if n <= 2:
            return dp[n]
        for _ in range(3, n + 1):
            dp[3] = (k - 1) * (dp[2] + dp[1])
            dp[1] = dp[2]
            dp[2] = dp[3]
        
        return dp[3]