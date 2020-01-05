class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        if not num1 and not num2:
            return 0
        
        num1 = num1.strip().strip('+')
        num2 = num2.strip().strip('+')
        
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        
        sums, carry = 0, 0
        res = ''
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0:
                sums += ord(num1[index1]) - ord('0')
                index1-= 1
            
            if index2 >= 0:
                sums += ord(num2[index2]) - ord('0')
                index2-= 1
            
            sums += carry
            res = str(sums % 10) + res
            carry = sums // 10
            sums = 0
            
        if carry > 0:
            res = str(carry) + res
            
        return res 
        
