'''
=> Naive DFS
'''
class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        if n == 1:
            return ["0", "1", "8"]
            
        res = []
        self.mirror = {
            '0': '0',
            '6': '9',
            '8': '8', 
            '1': '1',
            '9': '6'
        }
        self.dfs(n, 0, '', res)
        
        return res
        
    def dfs(self, n, start, tmp_string, res):
        if n % 2 == 1 and start == n // 2:
            tmp_len = len(tmp_string)
            for num in '018':
                res_string = tmp_string
                res_string += num
                for i in range(tmp_len - 1, -1, -1):
                    res_string += self.mirror[res_string[i]]
                res.append(res_string)
            return
        
        if n % 2 == 0 and start == n // 2:
            tmp_len = len(tmp_string)
            res_string = tmp_string
            for i in range(tmp_len - 1, -1, -1):
                res_string += self.mirror[tmp_string[i]]
            res.append(res_string)
            return
        
        if start != 0:
            for num in '01689':
                self.dfs(n, start + 1, tmp_string + num, res)
        
        if start == 0:
            for num in '1689':
                self.dfs(n, start + 1, tmp_string + num, res)
        

'''
=> Top-Down DFS
Time: O(5^n)
'''
class Solution2:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        
        self.res = ['']
        self.dfs(n, 0)
        
        return self.res
    
    def dfs(self, n, count):
        if n == 1:
            return ['0', '1', '8']
            
        if count >= n:
            return 
        
        if n % 2 == 1 and count == 0:
            count += 1
            for comb in self.res:
                res = []
                for num in '018':
                    res.append(num)
            self.res = res
            
        res = []
        for comb in self.res:
            res.append('6' + comb  + '9')
            res.append('9' + comb  + '6')
            res.append('8' + comb  + '8')
            res.append('1' + comb  + '1')
            if count < n - 2:
                res.append('0' + comb  + '0')
                
        self.res = res
        self.dfs(n, count + 2)