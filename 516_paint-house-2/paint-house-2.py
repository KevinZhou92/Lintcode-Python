'''
=> DP
Time: O(nk^2)
Space: O(k)
'''
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs:
            return 0
            
        houses = len(costs)
        colors = len(costs[0])
        
        # dp[i][k] minimum cost for painting ith housr with k th color
        dp = [costs[0][i] for i in range(colors)]
        
        for i in range(2, houses + 1):
            next_dp = [sys.maxsize] * colors
            for j in range(colors):
                for k in range(colors):
                    if k != j:
                        next_dp[j] = min(next_dp[j], dp[k] + costs[i - 1][j])
            dp = next_dp
            
        return min(dp)