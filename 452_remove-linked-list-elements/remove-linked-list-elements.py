'''
Note:
Be careful about all edge cases.
'''
class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        if not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next