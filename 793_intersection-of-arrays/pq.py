'''
=> PriorityQueue


Time: O(nklogk + nklogn), n arrs with k average elements
Spacs: O(k)
'''
from heapq import *
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        if not arrs:
            return 0
            
        queue = []    
        for index, arr in enumerate(arrs):
            if not arr:
                return 0
            arr.sort()
            # num, index
            heappush(queue, [arr[0], 0, index])
        
        last_value = None
        count = 0
        res = 0
        while queue:
            num, index, arr_index = heappop(queue)
            if not last_value or last_value != num:
                last_value = num
                count = 1
            else:
                count += 1
            if index + 1 < len(arrs[arr_index]):
                heappush(queue, [arrs[arr_index][index + 1], index + 1, arr_index])
                
            if count == len(arrs):
                res += 1
                
        return res
            