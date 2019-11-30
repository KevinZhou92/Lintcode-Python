"""
=> Greedy
2, 3, 1, 1, 4
at each point, check the max_right that we can each, as long as we can reach 
the point, we keep updating the max_right that we can reach

"""    
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
            
        max_right = A[0]
        for i in range(len(A)):
            if i <= max_right:
                max_right = max(max_right, A[i] + i)
            
            if max_right >= len(A) - 1:
                return True
        
        return False

"""
=> Dynamic programming

2 2 1 1 4

dp[i] -> represent can jump to j 
dp[i] = if dp[j] for j < i and j + A[j] >= A[i]
""" 
    def canJump2(self, A):
        
        
        dp = [0 for i in range(len(A))]
        dp[0] = 1
        
        for i in range(len(A)):
            for j in range(i):
                if dp[j] == 1 and j + A[j] >= i:
                    dp[i] = 1
                    break
                
        return dp[len(A) - 1] == 1
                
                