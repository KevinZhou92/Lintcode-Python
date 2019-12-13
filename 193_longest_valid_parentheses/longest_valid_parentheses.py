'''
")()())"
if ')'
    if left > 0, meet a right, add 2
    if left == 0, meet a right, start from cur pos and do the search

'''
class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        if not s:
            return 0
            
        res = 0
        left = 0
        while left < len(s):
            tmp_res = 0
            open_bracket = 0
            for right in range(left, len(s)):
                if s[right] == '(':
                    open_bracket += 1
                else:
                    if open_bracket == 0:
                        res = max(res, tmp_res)
                        break
                    else:
                        open_bracket -= 1
                        tmp_res += 2
                        if open_bracket == 0:
                            res = max(res, tmp_res)
            left += 1
            
            
        return res