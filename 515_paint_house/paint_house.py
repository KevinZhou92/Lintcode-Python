'''
=> DP
Time: O(rows)
Space: O(rows)
'''
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
            
        rows = len(costs)
        cols = len(costs[0])
        dp = [[sys.maxsize for i in range(cols)] for j in range(rows)]
        
        for i in range(cols):
            dp[0][i] = costs[0][i]
            
        for i in range(1, rows):
            for j in range(cols):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + costs[i][j])
                    
                if j - 2 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 2] + costs[i][j])
                    
                if j + 1 < cols:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + costs[i][j])
                    
                if j + 2 < cols:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 2] + costs[i][j])
                    
        return min(dp[rows - 1])