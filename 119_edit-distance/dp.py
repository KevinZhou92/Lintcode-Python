'''
=> DP
Time: O(n*m)
Space: O(n*m)
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
        if char equal, res = s1 - 1, s2 - 1
        if char not equal, minimum of
                           1 + res of s1 - 1, s2 - 1, # replace
                           1 + res of s1 - 1, s2      # delete
                           1 + res of s1, s2 - 1      # insert
        
        '''
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(0, len(word1) + 1):
            for j in range(0, len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1)
                
        return dp[len(word1)][len(word2)]
        
