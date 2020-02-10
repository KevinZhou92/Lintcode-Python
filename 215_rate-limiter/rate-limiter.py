from collections import defaultdict
class Solution:
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def __init__(self):
        self.durations = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400
        }
        self.limit_type = ['s', 'm', 'h', 'd']
        self.event_map = defaultdict(list)
    
    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        limit, limit_type = rate.split('/')
        limit = int(limit)
        start_time = timestamp
        
        limited = self.caculate_limitations(event, start_time, limit, limit_type)
        
        if increment and not limited:
            self.event_map[event].append(start_time)
            
        return limited
        
    def caculate_limitations(self, event_id, event_time, limit, limit_type):
        ts_list = self.event_map[event_id]
        start_time = event_time - self.durations[limit_type] + 1
        
        index = -1
        start, end = 0, len(ts_list) - 1
        if end == -1:
            return False
        while start + 1 < end:
            mid = start + (end - start) // 2
            if ts_list[mid] >= start_time:
                end = mid
            else:
                start = mid
                
        if ts_list[start] >= start_time:
            index = start
        elif ts_list[end] < start_time:
            index = end + 1
        else:
            index = end
            
        return (len(ts_list) - index) >= limit
        
        
        
            
        
    
        
        
        
        