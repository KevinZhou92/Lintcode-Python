"""
sort intervals
pick list[0] as cur_list
check if next interval can be merged
if can
    create a new range
if not
    add the cur_interval to res, set cur_interval = next_interval
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def cmp(x, y):
    return x.start - y.start

from functools import cmp_to_key
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if len(intervals) <= 1:
            return intervals
            
        res = []
        intervals.sort(key=lambda x: x.start)
        
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            if next_interval.start <= cur_interval.end:
                end = max(next_interval.end, cur_interval.end)
                cur_interval = Interval(cur_interval.start, end)
            else:
                res.append(cur_interval)
                cur_interval = next_interval
        res.append(cur_interval)

        return res

"""
Watch for case like:
[(2,3),(4,5),(6,7),(8,9),(1,10)]

The input doesn't imply that interval are partially overlapped, there could be a master interval that
will overlap all intervals
"""