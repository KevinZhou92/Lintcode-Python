class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        
        """
        x = 2, n = 3
        f(1) * f(1) * x
        x = 2, n = 4
        f(2) * f(2)
        
        x = 0, return 1
        x < 0, n odd, -
               n even, +
        n odd    
        x < 0, n < 0
        x 
        for every x, dvide by half, dfs
        memorization
        """
            
        self.res_map = {}
        res = self.dfs(abs(x), abs(n))
        if n < 0 and n % 2 == 1:
            if x < 0:
                return -1 / res
            else:
                return 1 / res
            
        if n < 0 and n % 2 == 0:
                return 1 / res
        
        if n > 0 and n % 2 == 1:  
            if x < 0:
                return -res
        
        return res
            
    def dfs(self, x, n):
        if n in self.res_map: 
            return self.res_map[n]
        
        if x == 0:
            return 0
        
        if n == 0:
            return 1
            
        if n == 1:
            return x
        
        res = 0
        if n % 2 == 0:
            res = self.dfs(x, n // 2) * self.dfs(x, n // 2)
        else:
            res = self.dfs(x, n // 2) * self.dfs(x, n // 2) * x
            
        self.res_map[n] = res
        
        return res

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if x == 0:
            return 0
        
        if n == 0:
            return 1
            
        if n < 0:
            return 1 / self.myPow(x, -n)
            
        if x < 0:
            x = x if n % 2 == 0 else -x
            
        tmp_res = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return tmp_res * tmp_res
        
        return tmp_res * tmp_res * x