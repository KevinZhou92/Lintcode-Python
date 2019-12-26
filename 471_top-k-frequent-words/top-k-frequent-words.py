'''
=> Bucket Sort
'''
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        from functools import cmp_to_key
        
        def cmp_func(x, y):
            # if count is equal
            if x[1] == y[1]:
                # compare word
                return -1 if y[0] < x[0] else 1 
            return x[1] - y[1]
        
        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
            
        freq_sorted = sorted(freq_dict.items(), key=cmp_to_key(cmp_func), reverse=True)
        
        res = []
        for i in range(k):
            res.append(freq_sorted[i][0])
            
        return res
