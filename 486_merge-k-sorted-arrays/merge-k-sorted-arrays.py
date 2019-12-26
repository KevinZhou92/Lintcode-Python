'''
=> MinHeap
Time: O(nlogk), n is the total number of numbers
Space: O(k)
'''
import heapq

class Num:
    def __init__(self, num, num_index, array_index):
        self.num = num
        self.num_index = num_index
        self.array_index = array_index
    
    def __lt__(self, other):
        return self.num < other.num
        
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        pq = []
        for index, array in enumerate(arrays):
            if array:
                heapq.heappush(pq, Num(array[0], 0, index))
        
        res = [] 
        while pq:
            cur_num = heapq.heappop(pq)
            num, num_index, array_index = cur_num.num, cur_num.num_index, cur_num.array_index
            res.append(num)
            if num_index + 1 < len(arrays[array_index]):
                heapq.heappush(pq, Num(arrays[array_index][num_index + 1], num_index + 1, array_index))
                
        return res
            
        
        
