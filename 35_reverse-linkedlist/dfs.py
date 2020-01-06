
"""
=> DFS
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