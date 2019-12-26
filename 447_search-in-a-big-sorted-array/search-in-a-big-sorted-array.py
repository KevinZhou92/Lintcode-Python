'''
find start and end
search between start and end
'''
class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
       
        start = 0
        end = 1
        while reader.get(end) < target:
            end *= 2
            
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
                
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        
        return -1