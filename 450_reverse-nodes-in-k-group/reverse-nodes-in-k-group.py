'''
=> DFS
Decompose it to smaller problem
Input:
list = 1->2->3->4->5->null
k = 2
Output:
2->1->4->3->5

0  ->1   ->2 
   head tail
count how many nodes are in list
move count // k times, connect the rest
return dummy.next

'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if k == 1:
            return head
            
        if not head:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        count = 0
        for i in range(k):
            count += 1
            head = head.next
            if not head:
                return dummy.next
            
        if count == k:
            prev =  self.reverseKGroup(head.next, k) 
            tail = dummy.next
            
            for i in range(k):
                tmp = tail.next
                tail.next = prev
                prev = tail
                tail = tmp
                
            tail = prev
            while tail.next:
                tail = tail.next
            
        return prev

'''
=> Iterative
1->2->3->4->5->null

count for total length

loop count / k times, revers nodes
    head of current k nodes, connect it with prev_tail
    
return 

none -> 1 -> 2 -> 3
prev head

'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution2:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        count = 0
        while head.next:
            count += 1
            head = head.next
            
        loops = count // k
        head = dummy.next
        prev = None
        prev_tail = dummy
        tail = None
        while loops > 0:
            tail = head
            for i in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            prev_tail.next = prev
            prev_tail = tail
            prev = None
            tail = None
            loops -= 1
        prev_tail.next = head
        
        return dummy.next

'''
0->(1->2)->3->4->5->null
1.head of k group
2.tail of prev k group
3.head of next k group

'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution3:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            count = 1
            tail = curr
            while tail and count < k:
                count += 1
                tail = tail.next
                if not tail:
                    return dummy.next
            
            next_cur = tail.next
            prev.next = tail
            self.reverse(curr, k)
            prev = curr
            curr.next = next_cur
            curr = next_cur
            
        return dummy.next
        
    def reverse(self, head, k):
        prev = None
        count = 0
        while count < k: 
            count += 1
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        