'''
=> Stack

Time: O(n^2)

'''
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        index = 0
        cur = ''
        while index < len(s):
            if s[index] == '(':
                stack.append(cur)
                cur = ''
            elif s[index] == ')':
                cur = cur[::-1]
                cur = stack.pop() + cur
            else:
                cur += s[index]
            index += 1
        
        return cur