'''
=> PriorityQueue

Time: O(nlogn + mlogm + (m + n)log(m + n))
'''
from heapq import *
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        queue = []
        for interval in A:
            heappush(queue, (interval[0], interval[1], 0))
        
        for interval in B:
            heappush(queue, (interval[0], interval[1], 1))
         
        res = []
        prev_start, prev_end, prev_type = heappop(queue)
        while queue:
            if prev_type == queue[0][2] or prev_end < queue[0][0]:
                prev_start, prev_end, prev_type = heappop(queue)
                continue
            cur_start, cur_end, cur_type = heappop(queue)
            res.append([cur_start, min(cur_end, prev_end)])
            if cur_end > prev_end:
                prev_start, prev_end, prev_type = cur_start, cur_end, cur_type
                
        return res
        