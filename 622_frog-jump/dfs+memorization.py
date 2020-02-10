class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        if not stones:
            return True
        
        memo = {}
        locations = {value: index for index, value in enumerate(stones)}
            
        return self.dfs(stones, 0, 1, locations, memo)
        
    def dfs(self, stones, index, last_step, locations, memo):
        if (index, last_step) in memo:
            return memo[(index, last_step)]
        
        if index == len(stones) - 1:
            return True
        
        res = False    
        for step in [last_step - 1, last_step, last_step + 1]:
            if step == 0:
                continue
            if step + stones[index] > stones[len(stones) - 1]:
                continue
            if step + stones[index] in locations:
                res |= self.dfs(stones, locations[stones[index] + step], step, locations, memo)
        
        memo[(index, last_step)] = res
        
        return res