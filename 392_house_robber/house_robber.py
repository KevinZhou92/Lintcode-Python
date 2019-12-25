'''
=> DP
Time: O(n)
Space: O(1)
'''
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        
        dp = [0] * (len(A) + 1)
        dp[0] = 0
        dp[1] = A[0]
        for i in range(2, len(A) + 1):
            dp[i] = max(dp[i - 2] + A[i - 1], dp[i - 1])
            
        return dp[-1]