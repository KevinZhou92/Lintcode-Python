from util_class import ListNode
class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        
        carry = 0
        while l1 or l2:
            if l1 and l2:
                tmp = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tmp = l1.val + carry
                l1 = l1.next
            else:
                tmp = l2.val + carry
                l2 = l2.next
            node = ListNode(tmp % 10)
            tail.next = node
            tail = node
            carry = tmp // 10
            
        if carry > 0:
            tail.next = ListNode(carry)
            
        return dummy.next
                
