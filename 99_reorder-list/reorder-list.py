"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head or not head.next or not head.next.next:
            return head
        # odd
        #  0 1 2 3 4
        #  0 4 1 3 2        
        # even 
        # 0 1 2 3
        # 0 3 1 2
        
        dummy = ListNode(0)
        dummy.next = head
        
        # get mid node
        mid = self.get_mid(head)
        
        # 3-> 4
        right = mid.next
        mid.next = None
        # 4->3
        right = self.reverse(right)
        
        return self.merge(dummy.next, right)
        
    def merge(self, left, right):
        
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            tail.next = left
            tail = left
            left = left.next
            tail.next = right
            tail = right
            right = right.next
            
        if left:
            tail.next = left
            
        return dummy.next
        
    def reverse(self, head):
        if not head:
            return head
            
        prev = None
        while head:
            tail = head.next
            head.next = prev
            prev = head
            head = tail
            
        return prev
        
    def get_mid(self, head):
        if not head or not head.next:
            return head
            
        slow = head
        fast = head.next
        # 1 2 3 4 5
        # s f
        #   s   f
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
            