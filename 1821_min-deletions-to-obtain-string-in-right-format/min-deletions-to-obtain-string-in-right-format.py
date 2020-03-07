class Solution:
    """
    @param s: the string
    @return: Min Deletions To Obtain String in Right Format
    """
    def minDeletionsToObtainStringInRightFormat(self, s):
        # write your code here
        if not s:
            return 0
            
        left_B, right_A = 0, sum([1 for char in s if char == 'A'])
        deletions = right_A
        for i in range(len(s)):
            if s[i] == 'A':
                right_A -= 1
            else:
                left_B += 1
            deletions = min(deletions, right_A + left_B)
        
        return deletions
        
        