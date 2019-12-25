'''
DP
Time: O(row * 3)
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
            
        # dp[i][k] is the minimum costs of ith house painted in kth color, total k is 3 in this case
        dp = [costs[0][i] for i in range(3)]
        for i in range(1, len(costs)):
            next_dp = [0] * 3
            next_dp[0] = min(dp[1] + costs[i][0], dp[2] + costs[i][0])
            next_dp[1] = min(dp[0] + costs[i][1], dp[2] + costs[i][1])
            next_dp[2] = min(dp[0] + costs[i][2], dp[1] + costs[i][2])
            dp = next_dp

        return min(dp)