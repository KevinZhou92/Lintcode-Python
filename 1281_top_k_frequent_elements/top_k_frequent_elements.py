class Element:
    def __init__(self, num, occurency):
        self.num = num
        self.occurency = occurency
    
Element.__lt__ = lambda x, y: x.occurency > y.occurency
# min heap
import heapq
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        if k == 0 or not nums:
            return []
            
        pq_map = {}
        for num in nums:
            if num not in pq_map:
                pq_map[num] = Element(num, 0)
            pq_map[num].occurency += 1
            
        pq = [value for value in pq_map.values()]
        heapq.heapify(pq)
        
        res= []
        for i in range(k):
            res.append(heapq.heappop(pq).num)
            
        return res
                
'''
=> Bucket Sort
O(N) Space and time
'''
class Solution2:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        
        freq_dict = {}
        
        res = []
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        freq_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            res.append(freq_sorted[i][0])
            
        return res