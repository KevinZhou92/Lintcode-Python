"""
[73, 74, 75, 71, 69, 72, 76, 73]
[1,   1,  4,  2,  1,  1, 0,  0]

if not stack or stack top > cur_tmp
    put index into queue
else:
    pop index, calculate distance, put it in res
"""
class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """
    def dailyTemperatures(self, temperatures):
        # Write your code here
        
        res = [0 for i in range(len(temperatures))]
        
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                    prev_index = stack.pop()
                    res[prev_index] = i - prev_index
            stack.append(i)
                    
        return res
            
                
        