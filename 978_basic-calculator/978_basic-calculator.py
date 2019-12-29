class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        result = 0
        sign = 1
        num = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char in '+-':
                result += num * sign 
                num = 0
                sign = -1 if char == '-' else 1
            elif char == ')':
                result += num * sign
                num = 0
                result *= stack.pop() # sign before (
                result += stack.pop() # result before (
                
            elif '0' <= char <= '9':
                num = num * 10 + int(char)
        
        if num > 0:
            result += num * sign
            
        return result