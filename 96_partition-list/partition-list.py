from util_class import ListNode
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        small_head = ListNode(0) 
        big_head = ListNode(0)
        s_head, b_head = small_head, big_head
        while head:
            tmp = head.next
            head.next = None
            if head.val < x:
                s_head.next = head
                s_head = s_head.next
            else:
                b_head.next = head
                b_head = b_head.next
            head = tmp    
        
        s_head.next = big_head.next
        
        return small_head.next