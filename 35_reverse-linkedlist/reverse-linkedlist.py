'''
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
            

        