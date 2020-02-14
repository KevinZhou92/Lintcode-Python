class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        if not s:
            return 0
        
        index = 0
        sign = '+'
        cur = 0
        stack = []
        while index < len(s):
            if s[index].isdigit():
                cur = cur * 10 + int(s[index])
            if not s[index].isdigit() and not s[index].isspace() or index == len(s) - 1:
                if sign == '+':
                    stack.append(cur)
                if sign == '-':
                    stack.append(-cur)
                if sign == '*':
                    stack.append(stack.pop() * cur)
                if sign == '/':
                    if stack[-1] <= 0:
                        stack.append(-(abs(stack.pop()) // cur))
                    else:
                        stack.append(stack.pop() // cur)
                cur = 0
                sign = s[index]
            index += 1
        
        return sum(stack)