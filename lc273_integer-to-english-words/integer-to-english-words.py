'''
=> Iteration

Time: O(n^2)
Space: O(n)
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        below20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty".split(' ')
        tens = 'Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred'.split(' ')
        thousands = ' Thousand Million Billion'.split(' ')
        
        if num == 0:
            return 'Zero'
        
        def helper(num):
            if num == 0:
                return ''
            
            if num <= 20:
                return below20[num - 1] + ' '
            
            if 20 <= num < 100:
                return tens[num // 10 - 1] + ' ' + helper(num % 10)
            
            return below20[num // 100 - 1] + ' Hundred ' + helper(num % 100)
        
        words = ''
        index = 0
        while num > 0:
            if num % 1000 > 0:
                words = helper(num % 1000) + thousands[index] + ' ' + words
            num = num // 1000
            index += 1
        
            
        return words.strip()