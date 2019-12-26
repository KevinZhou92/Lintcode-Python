'''
=> DP
Time: O(nk)
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
            first_min = -1
            second_min = -1
            for j in range(colors):
                if first_min == -1 or dp[j] < dp[first_min]:
                    second_min = first_min 
                    first_min = j
                elif second_min == -1 or dp[j] < dp[second_min]:
                    second_min = j
                    
            
            for k in range(colors):
                if k == first_min:
                    next_dp[k] = min(next_dp[k], dp[second_min] + costs[i - 1][k])
                else:
                    next_dp[k] = min(next_dp[k], dp[first_min] + costs[i - 1][k])
            dp = next_dp
            
        return min(dp)