"""
=> Top-down Merge Sort
[2->4->null,null,-1->null]
divide and conquer
mid = (start + end) // 2
start, mid
mid + 1, end

l1, l2 merge sort

"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
            
        return self.merge(lists, 0, len(lists) - 1)
        
    def merge(self, lists, start, end):
        if start == end:
            return lists[start]
            
        mid = start + (end - start) // 2
        l1 = self.merge(lists, start, mid)
        l2 = self.merge(lists, mid + 1, end)
        
        head = ListNode(0)
        dummy = head
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
                
            head = head.next
            
        if l1:
            head.next = l1
            
        if l2:
            head.next = l2
            
        return dummy.next
             

"""
=> Bottom-up
[2->4->null,null,-1->null]
each time we merge 2 lists 
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution2:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
            
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.merge(l1, l2)
                new_lists.append(merged)
            lists = new_lists
        
        return lists[0]
        
    def merge(self, l1, l2):
        head = ListNode(0)
        dummy = head
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            
        if l1:
            head.next = l1
            
        if l2:
            head.next = l2
            
        return dummy.next


"""
=> PriorityQueue
"""
import heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def cmp(x, y):
    return x.val < y.val

ListNode.__lt__ = cmp
# ListNode.__lt__ = lambda x, y: x.val < y.val
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        
        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, l)
            
        tail = ListNode(0)
        dummy = tail
        while pq:
            cur_node = heapq.heappop(pq)
            tail.next = cur_node
            tail = cur_node
            if cur_node.next:
                heapq.heappush(pq, cur_node.next)
            
        return dummy.next
            
        

