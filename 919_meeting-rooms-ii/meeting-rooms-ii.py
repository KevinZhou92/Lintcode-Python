'''
=> Sweep Line
Time: O(n)
'''
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        # [(0,30),(5,10),(15,20)]
        if not intervals:
            return 0
            
        time_points = []
        for interval in intervals:
            time_points.append([interval.start, True])
            time_points.append([interval.end, False])
        
        time_points.sort(key=lambda x:(x[0], x[1]))
        print(time_points)
        res = -sys.maxsize - 1
        tmp = 0
        for time_point in time_points:
            if time_point[1]:
                tmp += 1
            else:
                tmp -= 1
            res = max(res, tmp)
        
        return res