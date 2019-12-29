"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: a collection of intervals
    @return: the minimum number of intervals you need to remove
    """
    def eraseOverlapIntervals(self, intervals):
        # write your code here
        if not intervals:
            return 0
            
        '''
        [1,2], 
            [2,            5] 
                [3,        5] 
                  [4,5]
        
        '''
        intervals.sort(key=lambda x: x.start)
        res = 0
        end = intervals[0].end
        for interval in intervals[1:]:
            if end > interval.start:
                end = min(interval.end, end)
                res += 1
            else:
                end = interval.end
                
        return res
                
            