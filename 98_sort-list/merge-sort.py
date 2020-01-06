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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        mid = self.find_mid(head)
        right = mid.next
        mid.next = None
        sorted_left = self.sortList(head)
        sorted_right = self.sortList(right)
        
        return self.merge(sorted_left, sorted_right)
        
    def merge(self, l1, l2):
        dummy = ListNode(0)
        head = dummy
        
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
    
    def find_mid(self, head):
        slow = head
        fast = head.next
        # 1->2->3->4
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        