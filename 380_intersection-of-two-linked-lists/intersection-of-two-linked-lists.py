from util_class import ListNode
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None
            
        len_A = self.get_len(headA)
        len_B = self.get_len(headB)
        
        short_head, long_head = headA, headB
        if len_A > len_B:
            short_head, long_head = long_head, short_head
        
        for i in range(abs(len_A - len_B)):
            long_head = long_head.next
        
        while long_head != short_head:
            if not long_head or not long_head.next:
                return None
            long_head = long_head.next
            short_head = short_head.next
        
        
        return long_head
        
    def get_len(self, head):
        if not head:
            return 0
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        length = 0
        while head:
            head = head.next
            length += 1
            
        return length
    
            