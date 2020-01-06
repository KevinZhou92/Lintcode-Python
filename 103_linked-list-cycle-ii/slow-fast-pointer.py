'''
=> Slow-Faster Pointer
'''
class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None
            
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast != slow:
            return None
        
        fast = head
        slow = slow.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return fast
            
        