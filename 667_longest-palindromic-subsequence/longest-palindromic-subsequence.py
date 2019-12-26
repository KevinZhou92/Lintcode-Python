'''
=> DP
  c b b d
  0 1 2 3
0 1 1 1 0
1   1 2 0 
2     1 0
3       1

dp[i][j]:
if s[i] == s[j] dp[i + 1][j - 1] + 2
else max dp[i][j - 1], dp[i + 1][j]
'''

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        len_s = len(s)
        dp = [[0 for i in range(len_s + 1)] for j in range(len_s + 1)]
        for i in range(len_s, 0, -1):
            dp[i][i] = 1
            for j in range(i + 1, len_s + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i + 1][j])
                    
        return dp[1][len_s]
        
    