'''
A[(n−1)/2]
n = 1   0
    2   0
    3   1
    4   1
maxHeap 3 2 1   
minHeap 4 5   
minHeap and maxHeap, always pick from maxHeap
maxHeap represent lower part, minHeap represent bigger part

maxHeap - minHeap should less than 1
'''
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        import heapq
        
        minHeap = []
        maxHeap = []
        res = []
        
        for num in nums:
            if not maxHeap:
                # num in maxheap is negatived
                heapq.heappush(maxHeap, -num)
            elif not minHeap or num >= minHeap[0]:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappush(maxHeap, -num)
            
            if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
                maxHeap_num = -heapq.heappop(maxHeap)
                minHeap_num = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -minHeap_num)
                heapq.heappush(minHeap, maxHeap_num)
            
            if len(minHeap) - len(maxHeap) == 1:
                tmp_num = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -tmp_num)
                
            if len(maxHeap) - len(minHeap) > 1:
                tmp_num = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, tmp_num)
                
            res.append(-maxHeap[0])
            
        return res
        