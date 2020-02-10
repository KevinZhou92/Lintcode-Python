'''
=> Iteration

=> Time: O(n^2)
=> Space: O(n)

'''
class Solution:
    """
    @param str: String
    @return: String
    """
    def shortestPalindrome(self, string):
        # Write your code here
        if not string:
            return ''
        
        if len(string) == 1:
            return string
            
        index = len(string) - 1
        res = ''
        while index >= 0:
            substring = string[: index + 1]
            if substring == substring[::-1]:
                res = string[index + 1:][::-1] + string
                break
            index -= 1
        
        return res