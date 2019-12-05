"""
=> DFS
Input: 1->2->3->null
Output: 3->2->1->null

subproblem, reverse linkedlist starting with current head
need to reverse linkedlist starting with head.next and set head.nex = None
attach head to new_head

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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head.next:
            return head
            
        new_head = self.reverse(head.next)
        head.next = None
        
        dummy = new_head
        while new_head.next:
            new_head = new_head.next
        
        new_head.next = head
        
        return dummy

"""
=> DFS2
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    1->2->3
    """
    def reverse(self, head):
        # write your code here
        if not head.next or not head:
            return head
            
        # get the reversed head of linkedlist starting with head.next
        # so head.next becomes tail of the new linkedlist and head should be the next
        # after it, also remember to cut the original connecting after connnect origin head
        # to head.next
        new_head = self.reverse(head.next) 
        head.next.next = head
        head.next = None
        
        return new_head

"""
Iterative way
Usage of an extra node to keep refering the origin head
preserve tail.next in tmp
point tail.next to head
head = tail 
tail = tmp

remember to handle the origin head.next

or 
use a real dummy node to represent a fake head(None), the linkedlist would look like
prev cur
none->1->2->3->none

preserve cur.next
point cur.next to prev
now cur becomes prev and cur.next becomes cur

return prev
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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        old_head = head
        tail = head.next
        
        while tail:
            tmp = tail.next
            tail.next = head
            head = tail
            tail = tmp
        old_head.next = None
        
        return head
            

        