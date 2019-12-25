'''
=> DFS + Memorization
When define subproblem, we need to include all the requirements from the parent problem.
For example, in this solution, we define subproblem as: from given previous col, what's the 
minimum in the smaller costs array.
'''
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
        cols = len(costs[0])
        self.cost_map = {}
        
        return self.dfs(costs, 0, -1, cols)
        
    def dfs(self, costs, cur_row, prev_col, cols):
        res = sys.maxsize
        if (prev_col, cur_row) in self.cost_map:
            return self.cost_map[(prev_col, cur_row)]
        
        if cur_row == len(costs):
            return 0
            
        for i in range(cols):
            if i == prev_col:
                    continue
            res = min(res, self.dfs(costs, cur_row + 1, i, cols) + costs[cur_row][i])
        self.cost_map[(prev_col, cur_row)] = res
        
        return res