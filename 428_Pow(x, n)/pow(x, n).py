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


# Version 3 addition_mul record what part we are missing
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    
    """
    x^n = x^ (n / 2) * x^ (n / 2)
    n % 2 == 1? x^n = x^(n / 2) * x^ (n / 2) * x
    
    res= x
    (x * x) ^ (n /2)
    (x ^ 4) ^ (n / 4)
    
    4 / 2 = 2, 2/ 2 =1
    5 /2 = 2, 2/ 2 = 1
    
    2 20
    2 ^2 10
    2 ^4 5    -> (2^4)^4 * 2 ^ 4 -> 2^4 5
    2 ^8 2    -> (2^8)^2 * 2^ 4 -> 2^20
    2 ^16 1
    
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
            
        if x == 0:
            return 0
            
        if n < 0:
            n = -n 
            x = 1 / x
        
        res = x
        addition_mul = 1
        while n > 1:
            if n % 2 == 1:
                addition_mul *= res
            res = res * res
            n = n // 2
            
        return res * addition_mul

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
            x = 1 / x
            n = -n
            
        res = 1
        while n > 0:
            """
            every time n shrinks to half of its origin value, x should be squared
            if n is an odd, we should extrac '1' of current x, and the n becomes even, we just
            need to multiply the extracted x back to the result
            
            """
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
            
        return res