"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not intervals:
            return newInterval
            
        if not newInterval:
            intervals.sort(key=lambda interval: interval.start)
            return self.merge(intervals)
            
        intervals.append(newInterval)
        intervals.sort(key=lambda interval: interval.start)
        
        return self.merge(intervals)
        
    def merge(self, intervals):
        
        last_interval = intervals[0]
        res = []
        for interval in intervals[1:]:
            if interval.start <= last_interval.end:
                last_interval.end = max(last_interval.end, interval.end)
            else:
                res.append(last_interval)
                last_interval = interval
        res.append(last_interval)
        
        return res

"""
[(1, 2), (4, 9)] (2, 4)
                 (1, 9)
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution2:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not intervals:
            return newInterval
            
        res = []
        index = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                index += 1
                res.append(interval)
            elif interval.start <= newInterval.end:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
            elif interval.start > newInterval.end:
                res.append(interval)
                
        res.insert(index, newInterval)
        
        return res