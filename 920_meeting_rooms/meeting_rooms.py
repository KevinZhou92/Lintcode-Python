"""
Merge intervals, check if there is overlapping
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
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        
        if not intervals:
            return True
            
        intervals.sort(key=lambda interval: interval.start)
        
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if interval.start < last_interval.end:
                return False
            else:
                last_interval = interval
        
        return True

    