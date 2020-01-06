"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        
        # 7 -> 1-> 6
        # 5-> 9-> 2
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        dummy = ListNode(0)
        tail = dummy
        
        carry = 0
        while l1 or l2:
            if l1 and l2:
                tmp_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tmp_sum = l1.val + carry
                l1 = l1.next
            else:
                tmp_sum = l2.val + carry
                l2 = l2.next
            node = ListNode(tmp_sum % 10)
            tail.next = node
            tail = node
            carry = tmp_sum // 10
        
        if carry > 0:
            tail.next = ListNode(carry)
            
        return self.reverse(dummy.next)
    
    # 4-step reverse    
    def reverse(self, head):
        
        prev = None
        while head:
            tail = head.next
            head.next = prev
            prev = head
            head = tail
            
        return prev
            